from odoo import api, models, fields


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    quantity = fields.Float(compute='compute_multi_uom_qty', inverse='set_uom_qty', store=True)
    price_unit = fields.Float('Price Unit',
                              compute='compute_multi_price_unit',
                              inverse='set_multi_price_unit',
                              store=True,
                              digits='Multi Product Price')
    multi_price_unit = fields.Float('PriceUnit')
    multi_uom_qty = fields.Float(string='Qty',
                                 default=1.0,
                                 digits='Product Unit of Measure',
                                 help="The optional quantity expressed by this line, eg: number of product sold. "
                                      "The quantity is not a legal requirement but is very useful for some reports.")
    multi_uom_line_id = fields.Many2one('multi.uom.line', 'UoM')
    multi_uom_line_ids = fields.Many2many('multi.uom.line', compute='compute_multi_uom_line_ids')

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

    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super(AccountMoveLine, self)._onchange_product_id()
        line = self.product_id.multi_uom_line_ids.filtered(lambda l: l.uom_id.id == self.product_id.uom_id.id)
        self.multi_uom_line_id = line.id
        return res

    @api.depends('multi_uom_line_id', 'multi_uom_qty')
    def compute_multi_uom_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.quantity = rec.multi_uom_qty * rec.multi_uom_line_id.ratio
            else:
                rec.quantity = 0

    def set_uom_qty(self):
        for rec in self:
            if rec.multi_uom_line_id:
                rec.multi_uom_qty = rec.quantity / rec.multi_uom_line_id.ratio
