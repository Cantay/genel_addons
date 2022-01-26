# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import os.path


class Business(http.Controller):
    @http.route('/select/profile/', type="http", website=True, auth='public')
    def render_select_profile_view(self, **kw):
        return request.render('service_profiles.select_profile', {})
        # return request.render('service_profiles.create_profile', {})
    
    @http.route('/profiles/create/', type="http", website=True, auth='public')
    def rendirect_select_profile_view(self, **kw):
        print(kw.get('role'))
        role = kw.get('role')
        if role == "service":
            return request.render('service_profiles.create_profile', {})
        elif role == "advertiser":
            return request.render('ads_profiles.create_addprofiles', {})
        else:
            return request.render('service_profiles.create_profile', {}) 

            
    
    # render approved profile list
    @http.route('/busines/profiles/approved/', auth='public', website=True)
    def approved_list(self, **kw):
        profiles = request.env['res.partner'].sudo().search(
            [('status', '=', "approved")])
        print('printing profiles----------------------------', profiles)
        for profile in profiles:
            print('-----------printing profiles -----------------',
                  profile.businessName)

        return request.render('service_profiles.profiles_list_page', {
            'profiles': profiles
        })

    # redirect user to the address creation
    @http.route('/profiles/address', type="http", website=True, auth='public')
    def service_profile_create(self, **kw):
        # print('------------print POST data', kw)
        business_slug = kw.get('business_slug')
        user = request.env.user
        service = request.env['res.partner'].sudo().create(kw)
        service.write({'user_id': user.id})
        return request.render('service_profiles.create_address', {
            'business_slug': business_slug
        })

    @http.route("/check_business_slug", auth='public', methods=['POST'], type='json', csrf=False)
    def check_slug(self, **values):
        """
        check for existing business slugs asynchronously 
        """
        value = json.loads(request.httprequest.data)
        profiles = request.env['res.partner'].sudo().search(
            [('business_slug', '=', value.get('business_slug'))]
        )
        output = None
        if profiles.exists():
            output = {
                'data': {
                    'code': 200,
                    'exists': True,
                    'message': "Business Slug is already Taken"
                }
            }
        else:
            output = {
                'data': {
                    'code': 200,
                    'exists': False,
                    'message': "Business Slug is available"
                }
            }
        return output
