from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class BookingPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        res = super(BookingPortal, self)._prepare_home_portal_values(counters)
        res["booking_counts"] = request.env['booking.room'].search_count([])
        return res

    @http.route(['/my/bookings', '/my/bookings/page/<int:page>'], type='http', auth="user", website=True)
    def bookings_list_view(self, page=1, **kwargs):
        booking_obj = request.env['booking.room']
        total_bookings = booking_obj.sudo().search_count([])
        page_details = pager(url='/my/bookings',
                             total=total_bookings,
                             page=page,
                             step=10)

        bookings = booking_obj.sudo().search([], limit=10, offset=page_details['offset'])

        vals = {
            'bookings': bookings,
            'page_name': 'bookings_list_view',
            'pager': page_details,
        }
        return request.render('bookings_web_portal.bookings_list_view_portal', vals)

    @http.route(['/my/booking/<model("booking.room"):booking_id>'], type='http', auth="user", website=True)
    def bookings_form_view(self, booking_id, **kwargs):
        vals = {
            "booking": booking_id,
            'page_name': 'bookings_form_view',
        }

        booking_records = request.env['booking.room'].sudo().search([])
        booking_ids = booking_records.ids
        booking_index = booking_ids.index(booking_id.id)

        if booking_index != 0 and booking_ids[booking_index - 1]:
            vals['prev_record'] = '/my/booking/{}'.format(booking_ids[booking_index - 1])
        if booking_index < len(booking_ids) - 1 and booking_ids[booking_index + 1]:
            vals['next_record'] = '/my/booking/{}'.format(booking_ids[booking_index + 1])
        return request.render("bookings_web_portal.bookings_form_view_portal", vals)

    @http.route(['/my/booking/print/<model("booking.room"):booking_id>'], type='http', auth="user", website=True)
    def bookings_report_print(self, booking_id, **kwargs):
        print("=============== calling", booking_id)
        return self._show_report(model=booking_id,
                                 report_type="pdf",
                                 report_ref="room_booking.report_booking_card",
                                 download=True)
