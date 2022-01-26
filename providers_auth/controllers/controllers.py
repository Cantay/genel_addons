# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome as Home
from odoo.http import request
import json
import werkzeug.urls
import werkzeug.utils
from werkzeug.exceptions import BadRequest


class OAuthLogin(Home):
    def list_providers(self):
        try:
            providers = request.env['auth.oauth.provider'].sudo().search_read([('enabled', '=', True)])
        except Exception:
            providers = []
        for provider in providers:
            return_url = request.httprequest.url_root + 'auth_oauth/signin'
            return_url = return_url.replace('http://', 'https://')
            print ("return url " + return_url)
            state = self.get_state(provider)
            params = dict(
                response_type='token',
                client_id=provider['client_id'],
                redirect_uri=return_url,
                scope=provider['scope'],
                state=json.dumps(state),
            )
            provider['auth_link'] = "%s?%s" % (provider['auth_endpoint'], werkzeug.url_encode(params))
        return providers

# class TestModule(http.Controller):
#     @http.route('/test_module/test_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_module/test_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_module.listing', {
#             'root': '/test_module/test_module',
#             'objects': http.request.env['test_module.test_module'].search([]),
#         })

#     @http.route('/test_module/test_module/objects/<model("test_module.test_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_module.object', {
#             'object': obj
#         })
