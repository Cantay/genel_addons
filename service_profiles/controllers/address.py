from odoo.http import request
from odoo import http
import json


class BusinessAddress(http.Controller):
    @http.route('/images/create', type="http", website=True, auth='public')
    def service_address_create(self, **kw):
        print('------------print POST data', kw)
        business_slug = kw.pop('business_slug', None)
        location = kw.pop('location', None)
        profile = request.env['res.partner'].sudo().search([('business_slug', '=', business_slug)])
        profile.write(kw)
        return request.render('service_profiles.create_image', {
            'business_slug': business_slug
        })
