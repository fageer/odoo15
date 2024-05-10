from datetime import datetime
from odoo import api, fields, models, _

class BookingRoom(models.Model):
    _name = "booking.room"
    _description = "booking Room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'


    ref = fields.Char(string='Reference', readonly=True)
    room_id = fields.Many2one('room', string='Room', domain="[('state', '!=', 'not_available')]", tracking=True)
    # employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    start_date = fields.Datetime(string='From', tracking=True)
    end_date = fields.Datetime(string='To', tracking=True)
    status = fields.Boolean(string='Status', readonly=True)
    organizer = fields.Many2one('res.users', string='Organizer', required=True)
    room_state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done')], default='draft', string='Room Status', readonly=True, tracking=True)
    description = fields.Html(string='Description')
    agenda = fields.Html(string='Agenda')
    department_id = fields.Many2one('hr.department', string='Department')
    employee_lines_ids = fields.One2many('employee.lines', 'booking_id', string='Employee Lines', tracking=True)
    guests_lines_ids = fields.One2many('guests.lines', 'booking_id', string='Guests Lines', tracking=True)


    @api.onchange('organizer')
    def onchange_organizer(self):
        self.department_id = self.organizer.department_id


    def send_email(self):
        template = self.env.ref('room_booking.booking_room_mail_template')
        for rec in self:
            for guest in rec.guests_lines_ids:
                template.email_to = guest.email
                template.send_mail(guest.id, force_send=True)



    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('booking.room')

        new = super(BookingRoom, self).create(vals)
        user_id = new.organizer
        date_deadline = datetime.now()

        data = {
            'res_id': new.id,
            'res_model_id': self.env['ir.model'].search([('model', '=', 'booking.room')]).id,
            'user_id': user_id.id,
            'summary': 'foo bar',
            'activity_type_id': self.env.ref('mail.mail_activity_data_email').id,
            'date_deadline': date_deadline
        }
        print(data, "===================================")
        self.env['mail.activity'].create(data)
        return new


    def confirm(self):
        for rec in self:
            if rec.room_id.state == 'available':
                rec.room_id.state = 'not_available'
                rec.status = True
            rec.room_state = 'confirm'
        self.message_post(body="Room Booking Successfully")


    def meeting_done(self):

        bookings = self.env['booking.room'].search([('end_date', '<=', fields.Datetime.now()),
                                                    ('room_state', '=', 'confirm')])
        for rec in bookings:
            rec.room_state = 'done'
            rec.status = False
            rec.room_id.state = 'available'

            rec.message_post(body="Room Booking Done")



class EmployeeLines(models.Model):
    _name = "employee.lines"
    _description = "Employee Lines"


    employee_id = fields.Many2one('hr.employee', string='Employee')
    work_phone = fields.Char(string='Phone')
    work_email = fields.Char(string='Email')
    booking_id = fields.Many2one('booking.room')

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        self.work_phone = self.employee_id.work_phone
        self.work_email = self.employee_id.work_email




class GuestsLines(models.Model):
    _name = "guests.lines"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Guests Lines"


    guests_id = fields.Many2one('res.partner', string='Guests')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    booking_id = fields.Many2one('booking.room')

    @api.onchange('guests_id')
    def onchange_guests_id(self):
        self.phone = self.guests_id.phone
        self.email = self.guests_id.email
