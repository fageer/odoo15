from odoo import api, fields, models, _


class Room(models.Model):
    _name = "room"
    _description = "Room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'room_name'


    ref = fields.Char(string='Reference', readonly=True)
    room_name = fields.Char(string='Name', required=True, tracking=True)
    location_id = fields.Many2one('hr.work.location', string='Location', tracking=True)
    facility_lines_ids = fields.One2many('room.facility.lines', 'room_id', string='Facility Lines', tracking=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('not_available', 'Not Available')], default='available', string='Status', tracking=True)


    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('room')
        return super(Room, self).create(vals)




class RoomFacilityLines(models.Model):
    _name = "room.facility.lines"
    _description = "Room Facility Lines"


    facility_id = fields.Many2one('facilities.room', string='Facility')
    qty = fields.Integer(string='Quantity', default=1)
    room_id = fields.Many2one('room')



