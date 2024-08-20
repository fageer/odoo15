from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class ResPartnerPortal(CustomerPortal):
    pass
    # @http.route(['/new/cv'], type='http', method=['POST', 'GET'], auth="user", website=True)
    # def new_cv(self, **kwargs):
    #     # Fetch records to be used in the form
    #     partner_records = request.env['res.partner'].sudo().search([])
    #     country_records = request.env['res.country'].sudo().search([])
    #     city_records = request.env['res.country.state'].sudo().search([])
    #     job_records = request.env['jobs'].sudo().search([])
    #     skill_records = request.env['skills.tags'].sudo().search([])
    #     current_partner = request.env.user.partner_id
    #
    #     vals = {
    #         'partner_records': partner_records,
    #         'country_records': country_records,
    #         'city_records': city_records,
    #         'job_records': job_records,
    #         'skill_records': skill_records,
    #         'current_partner': current_partner,
    #         'page_name': 'new_cv'
    #     }
    #
    #     if request.httprequest.method == "POST":
    #         error_list = []
    #         if not kwargs.get('name_id'):
    #             error_list.append("Name field is mandatory.")
    #         if not kwargs.get('summary'):
    #             error_list.append("Summary field is mandatory.")
    #         if not error_list:
    #             # Handle many2many field
    #             skills_ids = kwargs.get('skills_ids', [])
    #             if isinstance(skills_ids, str):
    #                 skills_ids = [skills_ids]  # Convert to list if only one item selected
    #
    #             cv_vals = {
    #                 'image': kwargs.get('image'),
    #                 'name_id': kwargs.get('name_id'),
    #                 'email': kwargs.get('email'),
    #                 'job_title': kwargs.get('job_title'),
    #                 'phone_number': kwargs.get('phone_number'),
    #                 'country_id': kwargs.get('country_id'),
    #                 'city_id': kwargs.get('city_id'),
    #                 'summary': kwargs.get('summary'),
    #                 'skills_ids': [(6, 0, [int(skill_id) for skill_id in skills_ids])]
    #             }
    #             request.env['create.cv'].sudo().create(cv_vals)
    #             vals['success_msg'] = "CV Created Successfully!"
    #         else:
    #             vals['error_list'] = error_list
    #
    #     return request.render('cv_web_portal.new_cv_form_view_portal', vals)
