from odoo import api, fields, models, _

class FacilitiesRoom(models.Model):
    _name = "facilities.room"
    _description = "Facilities Room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'facility'


    ref = fields.Char(string='Reference', readonly=True)
    facility = fields.Char(string='Facility', required=True)

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('facilities.room')
        return super(FacilitiesRoom, self).create(vals)
