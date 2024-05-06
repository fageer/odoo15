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
    organizer = fields.Many2one('res.users', string='Organizer')
    room_state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done')], default='draft', string='Room Status', tracking=True)
    description = fields.Html(string='Description')
    employee_lines_ids = fields.One2many('employee.lines', 'booking_id', string='Employee Lines', tracking=True)
    guests_lines_ids = fields.One2many('guests.lines', 'booking_id', string='Guests Lines', tracking=True)



    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('booking.room')
        return super(BookingRoom, self).create(vals)


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
    booking_id = fields.Many2one('booking.room')




class GuestsLines(models.Model):
    _name = "guests.lines"
    _description = "Guests Lines"


    guests_id = fields.Many2one('res.partner', string='Guests')
    booking_id = fields.Many2one('booking.room')
