# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Busines(http.Controller):

     @http.route('/busines/profiles/approved/', auth='public', website=True)
     def approved_list(self, **kw):
        profiles = request.env['business.profile'].sudo().search([('status', '=', "approved")])
        print('printing profiles----------------------------', profiles)
        for profile in profiles:
            print('-----------printing profiles -----------------', profile.businessName)
        return request.render('busines.profiles_list_page', {
            'profiles': profiles
        })
        
     @http.route('/profiles/create/', type="http", website=True, auth='public')
     def book_webform(self, **kw):
        return request.render('busines.create_profile', {})

     @http.route('/profiles/create/action', type="http", website=True, auth='public')
     def library_book_create(self, **kw):
        print('------------print POST data', kw)
        businessSlug = kw.get('businessSlug')
        print(businessSlug)
        request.env['business.profile'].sudo().create(kw)
        return request.render('busines.create_profile', {})


#     @http.route('/busines/busines/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('busines.listing', {
#             'root': '/busines/busines',
#             'objects': http.request.env['business.profile'].search([]),
#         })

#     @http.route('/busines/busines/objects/<model("business.profile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('busines.object', {
#             'object': obj
#         })
