# -*- coding: utf-8 -*-
from odoo import models, fields

class AdsProfile(models.Model):
   
   
    _inherit = 'res.partner'
  
    bt_category = fields.Selection([
        ('saloon', 'Saloon'),
        ('restaurant', 'Restaurant')
    ], string='Category' )
    bt_title = fields.Char(string='Title')
    bt_description = fields.Text(string='Description')
    bt_status = fields.Selection([
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'rejected'),
    ], default='pending' ,string='Status')
    

