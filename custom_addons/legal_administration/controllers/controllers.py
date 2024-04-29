# -*- coding: utf-8 -*-
# from odoo import http


# class LegalAdministration(http.Controller):
#     @http.route('/legal_administration/legal_administration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/legal_administration/legal_administration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('legal_administration.listing', {
#             'root': '/legal_administration/legal_administration',
#             'objects': http.request.env['legal_administration.legal_administration'].search([]),
#         })

#     @http.route('/legal_administration/legal_administration/objects/<model("legal_administration.legal_administration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('legal_administration.object', {
#             'object': obj
#         })
