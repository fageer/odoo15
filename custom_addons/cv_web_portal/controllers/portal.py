from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager
import base64


class CvPortal(CustomerPortal):
    @http.route(['/new/cv'], type='http', method=['POST', 'GET'], auth="user", website=True)
    def new_cv(self, **kwargs):
        # Fetch records to be used in the form
        partner_records = request.env['res.partner'].sudo().search([])
        country_records = request.env['res.country'].sudo().search([])
        city_records = request.env['res.country.state'].sudo().search([])
        job_records = request.env['jobs'].sudo().search([])
        skill_records = request.env['skills.tags'].sudo().search([])
        current_partner = request.env.user.partner_id
        vals = {
            'partner_records': partner_records,
            'country_records': country_records,
            'city_records': city_records,
            'job_records': job_records,
            'skill_records': skill_records,
            'current_partner': current_partner,
            'page_name': 'new_cv'
        }

        if request.httprequest.method == "POST":
            error_list = []
            if not kwargs.get('name_id'):
                error_list.append("Name field is mandatory ❌.")
            if not kwargs.get('summary'):
                error_list.append("Summary field is mandatory ❌.")
            if not error_list:
                experience_lines = []
                index = 1
                while f'company_name_{index}' in kwargs:
                    print(f"Processing experience block {index}")
                    exp_vals = {
                        'company_name': kwargs.get(f'company_name_{index}'),
                        'job_position': kwargs.get(f'job_position_{index}'),
                        'experience_start_date': kwargs.get(f'experience_start_date_{index}'),
                        'experience_end_date': kwargs.get(f'experience_end_date_{index}'),
                        'experience_summary': kwargs.get(f'experience_summary_{index}'),
                    }
                    experience_lines.append((0, 0, exp_vals))
                    index += 1
                file = request.httprequest.files.get('image')
                cv_vals = {
                    'image': base64.b64encode(file.read()),
                    'name_id': kwargs.get('name_id'),
                    'email': kwargs.get('email'),
                    'job_title': kwargs.get('job_title'),
                    'phone_number': kwargs.get('phone_number'),
                    'country_id': kwargs.get('country_id'),
                    'city_id': kwargs.get('city_id'),
                    'summary': kwargs.get('summary'),
                    'experience_lines_ids': experience_lines,
                }
                print("Exp Lines: ", experience_lines)
                new_cv_id = request.env['create.cv'].sudo().create(cv_vals)
                vals['success_msg'] = "CV Created Successfully ✔!"
            else:
                vals['error_list'] = error_list
        return request.render('cv_web_portal.new_cv_form_view_portal', vals)

    def _prepare_home_portal_values(self, counters):
        res = super(CvPortal, self)._prepare_home_portal_values(counters)
        res["cv_counts"] = request.env['create.cv'].search_count([('name_id','=',request.env.user.partner_id.id)])
        return res

    @http.route(['/my/cvs', '/my/cvs/page/<int:page>'], type='http', auth="user", website=True)
    def cvs_list_view(self, page=1, **kwargs):
        cv_obj = request.env['create.cv']
        total_cvs = cv_obj.sudo().search_count([('name_id','=',request.env.user.partner_id.id)])
        page_details = pager(url='/my/cvs',
                             total=total_cvs,
                             page=page,
                             step=10)

        cvs = cv_obj.sudo().search([('name_id','=',request.env.user.partner_id.id)], limit=10, offset=page_details['offset'])

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

        cv_records = request.env['create.cv'].sudo().search([('name_id','=',request.env.user.partner_id.id)])
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
