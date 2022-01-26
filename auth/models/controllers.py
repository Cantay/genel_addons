from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo import http, _
from odoo.exceptions import UserError
import re


class AuthSignupStreet(AuthSignupHome):
    def _signup_with_values(self, token, values):
        context = self.get_auth_signup_qcontext()
        values.update({'contact_no': context.get('contact_no'),
                      'last_name': context.get('last_name')})
        # if re.match(r'^[0-9]+$', context.get('contact_no')) != None:
        # return True
        # else:
        #raise UserError(_("Please enter a valid telephone number"))
        super(AuthSignupStreet, self)._signup_with_values(token, values)

