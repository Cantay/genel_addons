from odoo import api, models, fields


class PurchaseOrderLine(models.Model):

    _inherit = 'purchase.order.line'

    product_qty = fields.Float(compute='compute_multi_uom_line_qty',
                               inverse='set_multi_uom_line_qty',
                               store=True, readonly=False)
    price_unit = fields.Float('Price Unit',
                              compute='compute_multi_price_unit',
                              inverse='set_multi_price_unit', store=True, digits='Multi Product Price')
    multi_price_unit = fields.Float('PriceUnit')
    purchase_uom_qty = fields.Float('UOM Qty', digits='Product Unit of Measure', default=1.0)
    multi_uom_line_id = fields.Many2one('multi.uom.line', 'Multi UOM Line', compute=False)
    multi_qty_received = fields.Float('Qty Received',
                                      digits='Product Unit of Measure',
                                      compute='_compute_multi_qty_received',
                                      store=True)
    multi_qty_invoiced = fields.Float('Qty Billed',
                                      digits='Product Unit of Measure',
                                      compute='_compute_multi_qty_invoiced',
                                      store=True)
    multi_uom_line_ids = fields.Many2many('multi.uom.line', compute='compute_multi_uom_line_ids')

    @api.onchange('product_qty', 'product_uom')
    def _onchange_quantity(self):
        super(PurchaseOrderLine, self)._onchange_quantity()
        self.compute_multi_price_unit()

    @api.depends('multi_uom_line_id', 'multi_price_unit')
    def compute_multi_price_unit(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.price_unit = rec.multi_price_unit / rec.multi_uom_line_id.ratio
            else:
                rec.price_unit = rec.multi_price_unit

    def set_multi_price_unit(self):
        for rec in self:
            rec.multi_price_unit = rec.price_unit * rec.multi_uom_line_id.ratio

    @api.depends('product_id')
    def compute_multi_uom_line_ids(self):
        for rec in self:
            rec.multi_uom_line_ids = rec.product_id.multi_uom_line_ids.ids

    @api.model
    def create(self, values):
        res = super(PurchaseOrderLine, self).create(values)
        if not res.multi_uom_line_id:
            res.onchange_product_id()
        return res

    @api.onchange('product_id')
    def onchange_product_id(self):
        res = super(PurchaseOrderLine, self).onchange_product_id()
        self.multi_uom_line_id = self.product_id.multi_uom_line_ids.filtered(
            lambda l: l.uom_id.id == self.product_id.uom_po_id.id
        ).id
        return res

    @api.depends('product_id', 'multi_uom_line_id', 'purchase_uom_qty')
    def compute_multi_uom_line_qty(self):
        for rec in self:
            rec.product_qty = rec.multi_uom_line_id.ratio * rec.purchase_uom_qty

    def set_multi_uom_line_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.purchase_uom_qty = rec.product_qty / rec.multi_uom_line_id.ratio
            else:
                rec.purchase_uom_qty = rec.product_qty

    @api.depends('multi_uom_line_id', 'qty_received')
    def _compute_multi_qty_received(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.multi_qty_received = rec.qty_received / rec.multi_uom_line_id.ratio
            else:
                rec.multi_qty_received = rec.qty_received

    @api.depends('multi_uom_line_id', 'qty_invoiced')
    def _compute_multi_qty_invoiced(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.multi_qty_invoiced = rec.qty_invoiced / rec.multi_uom_line_id.ratio
            else:
                rec.multi_qty_invoiced = rec.qty_invoiced

    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        values = super(PurchaseOrderLine, self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        values['multi_uom_line_id'] = self.multi_uom_line_id.id
        return values

    def _prepare_account_move_line(self, move=False):
        values = super(PurchaseOrderLine, self)._prepare_account_move_line(move)
        values['multi_uom_line_id'] = self.multi_uom_line_id.id
        return values

    @api.model
    def _prepare_purchase_order_line_from_procurement(self, product_id, product_qty, product_uom, company_id, values, po):
        res = super(PurchaseOrderLine, self)._prepare_purchase_order_line_from_procurement(product_id,
                                                                                           product_qty,
                                                                                           product_uom,
                                                                                           company_id,
                                                                                           values,
                                                                                           po)
        res['multi_uom_line_id'] = values.get('multi_uom_line_id')
        return res
