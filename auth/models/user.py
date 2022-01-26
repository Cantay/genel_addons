from odoo import api, fields, models

class ResUsersExt(models.Model):
    _inherit = 'res.users'

    contact_no = fields.Char(string='Telephone Number', required=True)
    last_name = fields.Char(string='Last Name', required=True)
   