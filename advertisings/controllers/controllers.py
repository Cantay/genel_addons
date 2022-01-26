# -*- coding: utf-8 -*-
# from odoo import http


# class Busines(http.Controller):
#     @http.route('/busines/busines/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/busines/busines/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('busines.listing', {
#             'root': '/busines/busines',
#             'objects': http.request.env['busines.busines'].search([]),
#         })

#     @http.route('/busines/busines/objects/<model("busines.busines"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('busines.object', {
#             'object': obj
#         })
