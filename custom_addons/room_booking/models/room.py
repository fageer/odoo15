from odoo import api, fields, models, _

class Room(models.Model):
    _name = "room"
    _description = "Room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'room_name'

    room_name = fields.Char(string='Name')
    location_id = fields.Many2one('hr.work.location', string='Location')
    facility_lines_ids = fields.One2many('room.facility.lines', 'room_id', string='Facility Lines')
    state = fields.Selection([
        ('available', 'Available'),
        ('not_available', 'Not Available')], default='available', string='Status')




class RoomFacilityLines(models.Model):
    _name = "room.facility.lines"
    _description = "Room Facility Lines"

    facility_id = fields.Many2one('facilities.room', string='Facility')
    qty = fields.Integer(string='Quantity', default=1)
    room_id = fields.Many2one('room')



