# -*- coding: utf-8 -*-
# from odoo import http


# class RoomBooking(http.Controller):
#     @http.route('/room_booking/room_booking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/room_booking/room_booking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('room_booking.listing', {
#             'root': '/room_booking/room_booking',
#             'objects': http.request.env['room_booking.room_booking'].search([]),
#         })

#     @http.route('/room_booking/room_booking/objects/<model("room_booking.room_booking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('room_booking.object', {
#             'object': obj
#         })
