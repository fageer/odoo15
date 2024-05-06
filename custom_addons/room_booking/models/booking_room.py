from odoo import api, fields, models, _

class BookingRoom(models.Model):
    _name = "booking.room"
    _description = "booking Room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_id'

    room_id = fields.Many2one('room', string='Room', domain="[('state', '!=', 'not_available')]")
    employee_id = fields.Many2one('hr.employee', string='Employee')
    start_date = fields.Datetime(string='From')
    end_date = fields.Datetime(string='To')



    def confirm(self):
        for rec in self:
            if rec.room_id.state == 'available':
                rec.room_id.state = 'not_available'
