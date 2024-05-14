from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    booking_id = fields.Many2one('booking.room', string="Booking", readonly=True)