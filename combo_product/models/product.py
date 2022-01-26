from odoo import api, models, fields


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    combo_product_ok = fields.Boolean('Combo Product')
    combo_item_ids = fields.One2many('combo.item', 'product_template_id', 'Combo Items')
    
    
