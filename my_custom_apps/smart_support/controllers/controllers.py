# -*- coding: utf-8 -*-
# from odoo import http


# class SmartSupport(http.Controller):
#     @http.route('/smart_support/smart_support/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_support/smart_support/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_support.listing', {
#             'root': '/smart_support/smart_support',
#             'objects': http.request.env['smart_support.smart_support'].search([]),
#         })

#     @http.route('/smart_support/smart_support/objects/<model("smart_support.smart_support"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_support.object', {
#             'object': obj
#         })
