from odoo import api, models, fields, _


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    product_uom_qty = fields.Float(compute='compute_product_uom_qty',
                                   inverse='set_multi_uom_qty',
                                   store=True,
                                   readonly=False)
    qty_delivered_manual = fields.Float(compute='compute_manual_delivered_qty',
                                        inverse='set_multi_qty_delivered_manual',
                                        store=True)
    multi_uom_line_id = fields.Many2one('multi.uom.line', 'UoM')
    multi_uom_qty = fields.Float('UOM Qty',
                                 digits='Product Unit of Measure',
                                 default=1.0)
    multi_qty_delivered = fields.Float('DeliveredQuantity',
                                       copy=False,
                                       compute='_compute_multi_qty_delivered',
                                       inverse='_inverse_multi_qty_delivered',
                                       store=True,
                                       digits='Product Unit of Measure',
                                       default=0.0)
    multi_qty_delivered_manual = fields.Float('DeliveredManually',
                                              copy=False,
                                              digits='Product Unit of Measure',
                                              default=0.0)
    multi_qty_to_invoice = fields.Float(compute='_get_to_multi_invoice_qty',
                                        string='Invoice Qty',
                                        store=True,
                                        digits='Product Unit of Measure')
    multi_qty_invoiced = fields.Float(compute='_compute_multi_qty_invoiced',
                                      string='Invoiced Qty',
                                      store=True,
                                      digits='Product Unit of Measure')
    multi_uom_line_ids = fields.Many2many('multi.uom.line', compute='compute_multi_uom_line_ids')

    @api.depends('product_id')
    def compute_multi_uom_line_ids(self):
        for rec in self:
            rec.multi_uom_line_ids = rec.product_id.multi_uom_line_ids.ids

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        line = self.product_id.multi_uom_line_ids.filtered(lambda l: l.uom_id.id == self.product_id.uom_id.id)
        self.multi_uom_line_id = line.id
        return res

    @api.depends('multi_uom_line_id', 'multi_uom_qty')
    def compute_product_uom_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.product_uom_qty = rec.multi_uom_qty * rec.multi_uom_line_id.ratio
            else:
                rec.product_uom_qty = 0

    def set_multi_uom_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.multi_uom_qty = rec.product_uom_qty / rec.multi_uom_line_id.ratio

    @api.depends('multi_uom_line_id', 'qty_invoiced')
    def _compute_multi_qty_invoiced(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.multi_qty_invoiced = rec.qty_invoiced / rec.multi_uom_line_id.ratio
            else:
                rec.multi_qty_invoiced = 0

    @api.depends('multi_uom_line_id', 'qty_to_invoice')
    def _get_to_multi_invoice_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.multi_qty_to_invoice = rec.qty_to_invoice / rec.multi_uom_line_id.ratio
            else:
                rec.multi_qty_to_invoice = 0

    @api.depends('multi_uom_line_id', 'qty_delivered')
    def _compute_multi_qty_delivered(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.multi_qty_delivered = rec.qty_delivered / rec.multi_uom_line_id.ratio
            else:
                rec.multi_qty_delivered = 0

    @api.depends('multi_uom_line_id', 'multi_qty_delivered')
    def _inverse_multi_qty_delivered(self):
        for rec in self:
            rec.qty_delivered = rec.multi_qty_delivered * rec.multi_uom_line_id.ratio

    @api.depends('multi_uom_line_id', 'multi_qty_delivered_manual')
    def compute_manual_delivered_qty(self):
        for rec in self:
            rec.qty_delivered_manual = rec.multi_qty_delivered_manual * rec.multi_uom_line_id.ratio

    def set_multi_qty_delivered_manual(self):
        for rec in self:
            rec.multi_qty_delivered_manual = rec.qty_delivered_manual * rec.multi_uom_line_id.ratio

    def _prepare_procurement_values(self, group_id=False):
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update({
            'multi_uom_line_id': self.multi_uom_line_id.id,
        })
        return values

    def _prepare_invoice_line(self, **optional_values):
        values = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        values['multi_uom_line_id'] = self.multi_uom_line_id.id
        return values
