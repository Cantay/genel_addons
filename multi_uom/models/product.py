from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    multi_uom_ok = fields.Boolean('Multi UOM', copy=False)
    multi_uom_line_ids = fields.One2many('multi.uom.line', 'product_tmpl_id', 'Multi UOM Lines')
    uom_category_id = fields.Many2one('uom.category', 'UOM Category', related='uom_id.category_id', store=True)

    # @api.constrains('multi_uom_ok', 'multi_uom_line_ids')
    # def _check_multi_uom_lines(self):
    #     for rec in self:
    #         product_uom = rec.uom_id.id
    #         purchase_uom = rec.uom_po_id.id
    #         uom_ids = rec.multi_uom_line_ids.uom_id.ids
    #         if rec.multi_uom_ok:
    #             if product_uom not in uom_ids:
    #                 raise ValidationError('Product UoM is missing in multi UOM lines.')
    #             if purchase_uom not in uom_ids:
    #                 raise ValidationError('Purchase UoM is missing in multi UOM lines.')


class MultiUOMLine(models.Model):

    _name = 'multi.uom.line'
    _description = 'Multi UOM Line'
    _order = 'ratio'
    _rec_name = 'uom_id'

    uom_id = fields.Many2one('uom.uom', 'UOM')
    price = fields.Float('Price')
    ratio = fields.Float('Ratio', compute=False)
    product_tmpl_id = fields.Many2one('product.template', 'Product Template')

    def _compute_quantity(self, qty):
        self.ensure_one()
        return qty * self.ratio
