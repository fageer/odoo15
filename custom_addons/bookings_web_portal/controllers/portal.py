from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class BookingPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        res = super(BookingPortal, self)._prepare_home_portal_values(counters)
        res["booking_counts"] = request.env['booking.room'].search_count([])
        return res

    @http.route(['/my/bookings', '/my/bookings/page/<int:page>'], type='http', website=True)
    def bookings_list_view(self, page=1, **kwargs):
        booking_obj = request.env['booking.room']
        total_bookings = booking_obj.search_count([])
        page_details = pager(url='/my/bookings',
                             total=total_bookings,
                             page=page,
                             step=2)
        bookings = booking_obj.search([], limit=2, offset=page_details['offset'])
        vals = {
            'bookings': bookings,
            'page_name': 'bookings_list_view',
            'pager': page_details,
        }
        return request.render('bookings_web_portal.bookings_list_view_portal', vals)

    @http.route(['/my/booking/<model("booking.room"):booking_id>'], type='http', website=True)
    def bookings_form_view(self, booking_id, **kwargs):
        vals = {
            "booking": booking_id,
            'page_name': 'bookings_form_view',
        }
        return request.render("bookings_web_portal.bookings_form_view_portal", vals)
