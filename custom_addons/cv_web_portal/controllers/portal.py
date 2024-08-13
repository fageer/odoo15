from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class CvPortal(CustomerPortal):
    @http.route(['/new/cv'], type='http', method=['POST', 'GET'], auth="user", website=True)
    def new_cv(self, **kwargs):
        partner_records = request.env['res.partner'].sudo().search([])
        country_records = request.env['res.country'].sudo().search([])
        city_records = request.env['res.country.state'].sudo().search([])
        job_records = request.env['jobs'].sudo().search([])
        skill_records = request.env['skills.tags'].sudo().search([])
        current_partner = request.env.user.partner_id
        if request.httprequest.method == "POST":
            print(kwargs)
            cv_vals = {
                'image': kwargs.get('image'),
                'name_id': kwargs.get('name_id'),
                'email': kwargs.get('email'),
                'job_title': kwargs.get('job_title'),
                'phone_number': kwargs.get('phone_number'),
                'country_id': kwargs.get('country_id'),
                'city_id': kwargs.get('city_id'),
                'summary': kwargs.get('summary')
            }
            request.env['create.cv'].sudo().create(cv_vals)
        else:
            print("calling GET Method =============")

        vals = {
                'partner_records': partner_records,
                'country_records': country_records,
                'city_records': city_records,
                'job_records': job_records,
                'skill_records': skill_records,
                'current_partner': current_partner,
                'page_name': 'new_cv'
                }
        return request.render('cv_web_portal.new_cv_form_view_portal', vals)

    def _prepare_home_portal_values(self, counters):
        res = super(CvPortal, self)._prepare_home_portal_values(counters)
        res["cv_counts"] = request.env['create.cv'].search_count([])
        return res

    @http.route(['/my/cvs', '/my/cvs/page/<int:page>'], type='http', auth="user", website=True)
    def cvs_list_view(self, page=1, **kwargs):
        cv_obj = request.env['create.cv']
        total_cvs = cv_obj.sudo().search_count([])
        page_details = pager(url='/my/cvs',
                             total=total_cvs,
                             page=page,
                             step=10)

        cvs = cv_obj.sudo().search([], limit=10, offset=page_details['offset'])

        vals = {
            'cvs': cvs,
            'page_name': 'cvs_list_view',
            'pager': page_details,
        }
        return request.render('cv_web_portal.cvs_list_view_portal', vals)

    @http.route(['/my/cv/<model("create.cv"):cv_id>'], type='http', auth="user", website=True)
    def cvs_form_view(self, cv_id, **kwargs):
        vals = {
            "cv": cv_id,
            'page_name': 'cvs_form_view',
        }

        cv_records = request.env['create.cv'].sudo().search([])
        cv_ids = cv_records.ids
        cv_index = cv_ids.index(cv_id.id)

        if cv_index != 0 and cv_ids[cv_index - 1]:
            vals['prev_record'] = '/my/cv/{}'.format(cv_ids[cv_index - 1])
        if cv_index < len(cv_ids) - 1 and cv_ids[cv_index + 1]:
            vals['next_record'] = '/my/cv/{}'.format(cv_ids[cv_index + 1])
        return request.render("cv_web_portal.cvs_form_view_portal", vals)

    @http.route(['/my/cv/print/<model("create.cv"):cv_id>'], type='http', auth="user", website=True)
    def cv_print(self, cv_id, **kwargs):
        print("=============== calling", cv_id)
        return self._show_report(model=cv_id,
                                 report_type="pdf",
                                 report_ref="create_cv.report_create_cv_without_photo",
                                 download=True)
