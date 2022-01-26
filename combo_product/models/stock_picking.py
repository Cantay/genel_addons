from odoo import api, models, fields, _ 


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    def _create_move_from_pos_order_lines(self, lines):
        res = super(StockPicking, self)._create_move_from_pos_order_lines(lines.filtered(lambda l: not l.product_id.combo_item_ids))
        combo_product_lines = lines.filtered(lambda l: l.product_id.combo_item_ids)
        for combo_product_line in combo_product_lines:
            combo_lines = combo_product_line.product_id.combo_item_ids
            for line in combo_lines:
                current_move = self.env['stock.move'].create({
                    'name': combo_product_line.name,
                    'product_uom': line.product_id.uom_id.id,
                    'picking_id': self.id,
                    'picking_type_id': self.picking_type_id.id,
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.quantity * combo_product_line.qty,
                    'state': 'draft',
                    'location_id': self.location_id.id,
                    'location_dest_id': self.location_dest_id.id,
                    'company_id': self.company_id.id,
                })
                current_move.quantity_done = line.quantity * combo_product_line.qty
        return res
