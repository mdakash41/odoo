# -*- coding: utf-8 -*-
# from odoo import http


# class MailThreadTester(http.Controller):
#     @http.route('/mail_thread_tester/mail_thread_tester/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mail_thread_tester/mail_thread_tester/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mail_thread_tester.listing', {
#             'root': '/mail_thread_tester/mail_thread_tester',
#             'objects': http.request.env['mail_thread_tester.mail_thread_tester'].search([]),
#         })

#     @http.route('/mail_thread_tester/mail_thread_tester/objects/<model("mail_thread_tester.mail_thread_tester"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mail_thread_tester.object', {
#             'object': obj
#         })
