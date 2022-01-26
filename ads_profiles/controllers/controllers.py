# -*- coding: utf-8 -*-
import json
from odoo import api, http
from odoo.http import request
import base64


class AdsProfile(http.Controller):

     @http.route('/addprofiles/create/', type="http", website=True, auth='public')
     def book_webform(self, **kw):
        return request.render('ads_profiles.create_addprofiles', {})

     @http.route('/addprofiles/create/action', type="http", website=True, auth='public')
     def library_book_create(self, **kw):
        print('------------print POST data', kw)
        user = request.env.user
        bt_title = kw.get('bt_title')
        service = request.env['res.partner'].sudo().create(kw)
        print("+++++++++++++++++profile get+++++++++++++++++++++", service)
        return request.render('ads_profiles.create_addprofileImages', {
           'bt_title': bt_title
        })

     @http.route('/addprofiles/images/create/action', type="http", website=True, auth='public')
     def profile_address_create(self, **kw):
        print('==============profile-update-data=============', kw)
        bt_title = kw.get('bt_title')

        profile = request.env['res.partner'].sudo().search([('bt_title', '=', bt_title)])
        

        image_1920 = kw.get('image_1920')
        imageFile=image_1920.read()
        d_imageFile = base64.b64encode(imageFile)

        
        profile.write({'image_1920': d_imageFile })
        print("+++++++++++++++++profile get+++++++++++++++++++++", profile)
        return request.render('ads_profiles.create_address', {
           'bt_title': bt_title
        })

     @http.route('/addprofiles/address/create/action', type="http", website=True, auth='public')
     def profile_adcreate(self, **kw):
        print('==============profile-update-data=============', kw)
        bt_title = kw.get('bt_title')
        profile = request.env['res.partner'].sudo().search([('bt_title', '=', bt_title)])
        print('==============profile=============', profile)
        street = kw.get('street_ads')
        street2 = kw.get('street2_ads')
        city = kw.get('city_ads')
        province = kw.get('province_ads')
        zip = kw.get('code_ads')
        phone = kw.get('phone_ads')
        mobile = kw.get('mobile_ads')
        email = kw.get('email_ads')
        profile.write({'street': street, 'street2': street2, 'city': city, 'province': province,
                      'zip': zip, 'phone': phone, 'mobile': mobile, 'email': email})
        print("+++++++++++++++++profile get+++++++++++++++++++++", profile)
        return request.render('ads_profiles.create_addprofiles', {})

     @http.route("/check_title", auth='public', methods=['POST'], type='json', csrf=False)
     def check_slug(self, **values):
        """
        check for existing business slugs asynchronously 
        """
        value = json.loads(request.httprequest.data)
        profiles = request.env['res.partner'].sudo().search(
            [('bt_title', '=', value.get('bt_title'))]
        )
        output = None
        if profiles.exists():
            output = {
                'data': {
                    'code': 200,
                    'exists': True,
                    'message': "Title is already Taken"
                }
            }
        else:
            output = {
                'data': {
                    'code': 200,
                    'exists': False,
                    'message': "Title is available"
                }
            }
        return output


     