# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class service_profiles(models.Model):
#     _name = 'service_profiles.service_profiles'
#     _description = 'service_profiles.service_profiles'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class ServiceProfile(models.Model):
    _sql_constraints = [
        ('business_slug', 'unique (business_slug)', 'The field  must be unique  !')
    ]
    _inherit = 'res.partner'

    business_slug = fields.Char()
    status = fields.Selection([
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'rejected'),
    ], default='pending')
    businessType = fields.Selection([
        ('saloon', 'Saloon'),
        ('restaurant', 'Restaurant')
    ], )
    description = fields.Text()

