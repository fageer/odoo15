# -*- coding: utf-8 -*-
# from odoo import http


# class BranchTask(http.Controller):
#     @http.route('/branch_task/branch_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/branch_task/branch_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('branch_task.listing', {
#             'root': '/branch_task/branch_task',
#             'objects': http.request.env['branch_task.branch_task'].search([]),
#         })

#     @http.route('/branch_task/branch_task/objects/<model("branch_task.branch_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('branch_task.object', {
#             'object': obj
#         })
