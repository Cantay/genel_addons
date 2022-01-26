# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Advertisement(models.Model):
    _name = 'billionthings.advertisement'
    _description = 'Advertisement'

    category = fields.Selection([
        ('option 1', 'Option 1'),
        ('option 2', 'Option 2'),
        ('option 3', 'Option 3'),
    ], string="Category")
    date_start = fields.Date(string="Start Date")
    artWork = fields.Char(string="Art Work")
    placement = fields.Char(string="Placement")
    package = fields.Selection([
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ], string="Package")
    instructions = fields.Text(string='Instructions')


