# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class BusinesAddress(http.Controller):

     @http.route('/profiles/address/create/action', type="http", website=True, auth='public')
     def profile_address_create(self, **kw):
        print('==============profile-update-data=============', kw)
        businessSlug = kw.get('businessSlug')
        profile = request.env['business.profile'].sudo().search([('businessSlug', '=', businessSlug)])
        print('==============profile=============',profile)
        no = kw.get('no')
        addressLine1 = kw.get('addressLine1')
        addressLine2 = kw.get('addressLine2')
        province = kw.get('province')
        postalCode = kw.get('postalCode')
        telephone1 = kw.get('telephone1')
        telephone2 = kw.get('telephone2')
        email = kw.get('email')
        locationl = kw.get('locationl')
        profile.write({'no': no , 'addressLine1': addressLine1, 'addressLine2': addressLine2, 'province': province, 'postalCode': postalCode, 'telephone1': telephone1, 'telephone2': telephone2, 'email': email, 'locationl': locationl})
        print("+++++++++++++++++profile get+++++++++++++++++++++", profile)
        return request.render('busines.create_profile', {})
