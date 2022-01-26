from odoo import models, fields, api

class Category(models.Model):
    _sql_constraints = [
        ('name', 'unique (name)', 'The field  must be unique  !')
    ]
    _name = 'service.category'

    name = fields.Char()
    description = fields.Text()

