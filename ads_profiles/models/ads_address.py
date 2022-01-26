# -*- coding: utf-8 -*-

from odoo import models, fields, api



class AdsAddress(models.Model):
    _inherit = 'res.partner'

    province= fields.Char(string="Province")


