from odoo import models, fields, api


class Gallery(models.Model):
    _name = 'service.gallery'

    image = fields.Binary(string='Service Image')
    business_id = fields.Many2one('res.partner', string='Business')
    
        
