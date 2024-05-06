from odoo import api, fields, models, _

class BookingRoom(models.Model):
    _name = "booking.room"
    _description = "booking Room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_id'


    ref = fields.Char(string='Reference', readonly=True)
    room_id = fields.Many2one('room', string='Room', domain="[('state', '!=', 'not_available')]", tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking=True)
    start_date = fields.Datetime(string='From', tracking=True)
    end_date = fields.Datetime(string='To', tracking=True)
    status = fields.Boolean(string='Status', readonly=True)


    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('booking.room')
        return super(BookingRoom, self).create(vals)


    def confirm(self):
        for rec in self:
            if rec.room_id.state == 'available':
                rec.room_id.state = 'not_available'
                rec.status = True


    def meeting_done(self):
        for rec in self:
            if rec.room_id.state == 'not_available':
                rec.room_id.state = 'available'
                rec.status = False

