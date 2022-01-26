from odoo import models
from odoo.tools import float_compare
from itertools import groupby


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    # Not to merge moves
    def action_confirm(self):
        self._check_company()
        self.mapped('package_level_ids').filtered(lambda pl: pl.state == 'draft' and not pl.move_ids)._generate_moves()
        # call `_action_confirm` on every draft move
        self.mapped('move_lines')\
            .filtered(lambda move: move.state == 'draft')\
            ._action_confirm(merge=False)

        # run scheduler for moves forecasted to not have enough in stock
        self.mapped('move_lines').filtered(lambda move: move.state not in ('draft', 'cancel', 'done'))._trigger_scheduler()
        return True

    # POS Related Methods
    def _prepare_stock_move_vals(self, first_line, order_lines):
        values = super(StockPicking, self)._prepare_stock_move_vals(first_line, order_lines)
        values['multi_uom_line_id'] = first_line.multi_uom_line_id.id
        return values

    # POS Related Methods
    def _create_move_from_pos_order_lines(self, lines):
        self.ensure_one()
        lines_by_product = groupby(sorted(lines, key=lambda l: l.product_id.id), key=lambda l: l.product_id.id)
        for product, product_lines in lines_by_product:
            products_grouped_by_uom = groupby(sorted(product_lines, key=lambda l: l.multi_uom_line_id.id), key=lambda l: l.multi_uom_line_id.id)
            for uom, lines in products_grouped_by_uom:
                order_lines = self.env['pos.order.line'].concat(*lines)
                first_line = order_lines[0]
                current_move = self.env['stock.move'].create(
                    self._prepare_stock_move_vals(first_line, order_lines)
                )
                confirmed_moves = current_move._action_confirm(merge=False)
                for move in confirmed_moves:
                    if first_line.product_id == move.product_id and first_line.product_id.tracking != 'none':
                        if self.picking_type_id.use_existing_lots or self.picking_type_id.use_create_lots:
                            for line in order_lines:
                                sum_of_lots = 0
                                for lot in line.pack_lot_ids.filtered(lambda l: l.lot_name):
                                    if line.product_id.tracking == 'serial':
                                        qty = 1
                                    else:
                                        qty = abs(line.qty)
                                    ml_vals = move._prepare_move_line_vals()
                                    ml_vals.update({'qty_done':qty})
                                    if self.picking_type_id.use_existing_lots:
                                        existing_lot = self.env['stock.production.lot'].search([
                                            ('company_id', '=', self.company_id.id),
                                            ('product_id', '=', line.product_id.id),
                                            ('name', '=', lot.lot_name)
                                        ])
                                        if not existing_lot and self.picking_type_id.use_create_lots:
                                            existing_lot = self.env['stock.production.lot'].create({
                                                'company_id': self.company_id.id,
                                                'product_id': line.product_id.id,
                                                'name': lot.lot_name,
                                            })
                                        quant = existing_lot.quant_ids.filtered(lambda q: q.quantity > 0.0 and q.location_id.parent_path.startswith(move.location_id.parent_path))[-1:]
                                        ml_vals.update({
                                            'lot_id': existing_lot.id,
                                            'location_id': quant.location_id.id or move.location_id.id
                                        })
                                    else:
                                        ml_vals.update({
                                            'lot_name': lot.lot_name,
                                        })
                                    self.env['stock.move.line'].create(ml_vals)
                                    sum_of_lots += qty
                                if abs(line.qty) != sum_of_lots:
                                    difference_qty = abs(line.qty) - sum_of_lots
                                    ml_vals = current_move._prepare_move_line_vals()
                                    if line.product_id.tracking == 'serial':
                                        ml_vals.update({'qty_done': 1})
                                        for i in range(int(difference_qty)):
                                            self.env['stock.move.line'].create(ml_vals)
                                    else:
                                        ml_vals.update({'qty_done': difference_qty})
                                        self.env['stock.move.line'].create(ml_vals)
                        else:
                            move._action_assign()
                            for move_line in move.move_line_ids:
                                move_line.qty_done = move_line.product_uom_qty
                            if float_compare(move.product_uom_qty, move.quantity_done, precision_rounding=move.product_uom.rounding) > 0:
                                remaining_qty = move.product_uom_qty - move.quantity_done
                                ml_vals = move._prepare_move_line_vals()
                                ml_vals.update({'qty_done':remaining_qty})
                                self.env['stock.move.line'].create(ml_vals)

                    else:
                        move._action_assign()
                        for move_line in move.move_line_ids:
                            move_line.qty_done = move_line.product_uom_qty
                        if float_compare(move.product_uom_qty, move.quantity_done, precision_rounding=move.product_uom.rounding) > 0:
                            remaining_qty = move.product_uom_qty - move.quantity_done
                            ml_vals = move._prepare_move_line_vals()
                            ml_vals.update({'qty_done':remaining_qty})
                            self.env['stock.move.line'].create(ml_vals)
                        move.quantity_done = move.product_uom_qty


