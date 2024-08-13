from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class CvPortal(CustomerPortal):
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

    # @http.route(['/my/booking/print/<model("booking.room"):booking_id>'], type='http', auth="user", website=True)
    # def bookings_report_print(self, booking_id, **kwargs):
    #     print("=============== calling", booking_id)
    #     return self._show_report(model=booking_id,
    #                              report_type="pdf",
    #                              report_ref="room_booking.report_booking_card",
    #                              download=True)
