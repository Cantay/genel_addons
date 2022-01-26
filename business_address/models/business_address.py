# -*- coding: utf-8 -*-

from odoo import models, fields, api



class BusinessAddress(models.Model):
    _inherit = 'business.profile'

    #Business Address - Add the location address of your business
    no= fields.Char(string="No")
    addressLine1= fields.Char(string="Address Line 1")
    addressLine2= fields.Char(string="Address Line 2")
    province= fields.Char(string="Province")
    postalCode= fields.Char(string="Postal Code")
    telephone1= fields.Char(string="Telephone 1")
    telephone2= fields.Char(string="Telephone 2")
    email= fields.Char(string="Email")
    locationl= fields.Char(string="Location l")



