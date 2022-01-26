from odoo import api, models, fields


class ComboItem(models.Model):

    _name = 'combo.item'
    _description = 'Combo Item'

    product_id = fields.Many2one('product.product', 'Product')
    quantity = fields.Float('Quantity', default=1)
    remarks = fields.Char('Remarks')
    product_template_id = fields.Many2one('product.template', 'Product Template')

