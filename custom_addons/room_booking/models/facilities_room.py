from odoo import api, fields, models, _

class FacilitiesRoom(models.Model):
    _name = "facilities.room"
    _description = "Facilities Room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'facility'


    facility = fields.Char(string='Facility', required=True, tracking=True)


