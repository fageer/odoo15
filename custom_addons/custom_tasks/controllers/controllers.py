# -*- coding: utf-8 -*-
# from odoo import http


# class CustomTasks(http.Controller):
#     @http.route('/custom_tasks/custom_tasks', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_tasks/custom_tasks/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_tasks.listing', {
#             'root': '/custom_tasks/custom_tasks',
#             'objects': http.request.env['custom_tasks.custom_tasks'].search([]),
#         })

#     @http.route('/custom_tasks/custom_tasks/objects/<model("custom_tasks.custom_tasks"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_tasks.object', {
#             'object': obj
#         })
