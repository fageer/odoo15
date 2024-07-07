import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date
from dateutil import relativedelta


class RoomBookingReportWizard(models.TransientModel):
    _name = "room.booking.report.wizard"
    _description = 'Room Booking Report Wizard'

    organizer_id = fields.Many2one('res.users', string='Organizer', default=lambda self: self.env.user.id)
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')


    def action_print_report(self):
        domain = []
        organizer_id = self.organizer_id
        if organizer_id:
            domain += [('organizer', '=', organizer_id.id)]

        date_from = self.date_from
        if date_from:
            domain += [('create_date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('create_date', '<=', date_to)]
        print("domain", domain)

        bookings = self.env['booking.room'].search_read(domain)
        print("========================================= Reporting", bookings)
        data = {
            'form_data': self.read()[0],
            'bookings': bookings,
        }
        return self.env.ref('room_booking.action_report_booking').report_action(self, data=data)


