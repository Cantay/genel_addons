from odoo import api, models, fields, _


class PosOrder(models.Model):

    _inherit = 'pos.order'

    def _prepare_invoice_line(self, order_line):
        values = super(PosOrder, self)._prepare_invoice_line(order_line)
        values['multi_uom_line_id'] = order_line.multi_uom_line_id.id
        return values


class PosOrderLine(models.Model):

    _inherit = 'pos.order.line'

    qty = fields.Float(compute='_compute_multi_qty', inverse='_set_multi_qty', store=True)
    pos_uom_id = fields.Many2one('uom.uom', 'Multi UoM')
    pos_uom_qty = fields.Float('UOM Qty', digits='Product Unit of Measure')
    multi_uom_line_id = fields.Many2one('multi.uom.line', 'Multi UoM Line')

    @api.depends('pos_uom_qty', 'multi_uom_line_id')
    def _compute_multi_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.qty = rec.pos_uom_qty * rec.multi_uom_line_id.ratio
            else:
                rec.qty = rec.pos_uom_qty

    @api.depends('qty', 'multi_uom_line_id')
    def _set_multi_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.pos_uom_qty = rec.qty / rec.multi_uom_line_id.ratio
            else:
                rec.pos_uom_qty = rec.qty

    def _order_line_fields(self, line, session_id=None):
        line = super(PosOrderLine, self)._order_line_fields(line, session_id)
        values = line[2]
        qty = values['qty']
        pos_uom_id = values.get('pos_uom_id', False)
        product = self.env['product.product'].browse(values.get('product_id', False))
        values['pos_uom_qty'] = qty
        if pos_uom_id:
            multi_uom_line = product.multi_uom_line_ids.filtered(lambda l: l.uom_id.id == pos_uom_id)
            values['qty'] *= multi_uom_line.ratio
            values['multi_uom_line_id'] = multi_uom_line.id
        elif values.get('multi_uom_line_id', False):
            multi_uom_line = self.env['multi.uom.line'].browse(values.get('multi_uom_line_id', False))
            values['qty'] *= multi_uom_line.ratio
            values['multi_uom_line_id'] = multi_uom_line.id
        else:
            values['multi_uom_line_id'] = product.multi_uom_line_ids.filtered(lambda l: l.uom_id.id == product.uom_id.id).id
        return line

    def _export_for_ui(self, orderline):
        values = super(PosOrderLine, self)._export_for_ui(orderline)
        if orderline.pos_uom_id:
            values['qty'] = orderline.pos_uom_qty
        values['multi_uom_line_id'] = orderline.multi_uom_line_id.id
        return values

