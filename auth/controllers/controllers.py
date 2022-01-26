import json
from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo import api, http
from odoo.http import request
import base64


class AuthSignupStreet(AuthSignupHome):
    def _signup_with_values(self, token, values):
        context = self.get_auth_signup_qcontext()
        values.update({'contact_no': context.get('contact_no'),'last_name': context.get('last_name'),'first_name': context.get('first_name')})
        super(AuthSignupStreet, self)._signup_with_values(token, values)
    
    
    @http.route("/check_email", auth='public', methods=['POST'], type='json', csrf=False)
    def check_slug(self, **values):
        """
        check for existing email asynchronously 
        """
        value = json.loads(request.httprequest.data)
        profiles = request.env['res.partner'].sudo().search(
            [('login', '=', value.get('login'))]
        )
        output = None
        if profiles.exists():
            output = {
                'data': {
                    'code': 200,
                    'exists': True,
                    'message': "Email is already Taken"
                }
            }
        else:
            output = {
                'data': {
                    'code': 200,
                    'exists': False,
                    'message': "Email is available"
                }
            }
        return output