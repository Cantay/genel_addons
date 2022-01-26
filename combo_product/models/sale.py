from odoo import api, models, fields


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('order_line')
    def get_combo_products(self):
        combo_lines = self.order_line.browse([])
        lines = self.order_line
        regular_lines = lines.filtered(lambda l: not l.is_combo_line)
        for line in regular_lines:
            if not (line.product_id.combo_product_ok and line.product_id.combo_item_ids):
                continue
            combo_lines |= self.env['sale.order.line'].new({
                'name': f'Combo Products of {line.product_id.name}',
                'display_type': 'line_section',
                'qty_delivered_method': 'manual',
                'is_combo_line': True,
            })
            for combo_line in line.product_id.combo_item_ids:
                new_line = self.env['sale.order.line'].new({
                    'name': combo_line.product_id.name,
                    'product_id': combo_line.product_id.id,
                    'product_uom_qty': combo_line.quantity * line.product_uom_qty,
                    'is_combo_line': True,
                    'state': 'draft',
                })
                new_line.product_id_change()
                combo_lines |= new_line
        
        combo_lines |= regular_lines
        self.order_line = combo_lines


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    is_combo_line = fields.Boolean('Is Combo Line?')
