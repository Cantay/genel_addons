from odoo import http
from odoo.http import request
import base64

class BusinessImage(http.Controller):
    @http.route('/images/create/', type="http", website=True, auth='public')
    def service_images_webform(self, **kw):
        business_slug = kw.pop('business_slug', None)
        return request.render('service_profiles.create_image', {})

    @http.route('/images/create/action', type="http", website=True, auth='public')
    def service_images_action_webform(self, **kw):
        business_slug = kw.pop('business_slug', None)
        business = request.env['res.partner'].sudo().search(
            [('business_slug', '=', business_slug)]
        )
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if 'images' in request.params:
            attached_files = request.httprequest.files.getlist('images')
            for file_ in attached_files:
                image = file_.read()
                image_as_bytes = base64.b64encode(image)
                value = {
                    'image': image_as_bytes,
                    'business_id': business.id
                }
                print(value)
                image_obj = request.env['service.gallery'].sudo().create(value)
        return request.render('service_profiles.create_image', {})