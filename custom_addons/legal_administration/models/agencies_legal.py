from odoo import api, fields, models


class AgenciesLegal(models.Model):
    _name = "agencies.legal"
    _description = "Agencies Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'tawkeel_number'
    
    tawkeel_number = fields.Char(string='Tawkeel Number')
    almwakkal = fields.Char(string='Almwakkal', required=True) 
    almwakkel = fields.Many2one('res.partner', string='Almwakkel', required=True)
    tawkeel_date = fields.Date(string='Tawkeel Date', required=True)
    tawkeel_expires = fields.Date(string='Tawkeel Expires', required=True)
    tawkeel_attached = fields.Binary(string='Tawkeel Attached', required=True)
    
    
    @api.model
    def create(self, vals):
        vals['tawkeel_number'] = self.env['ir.sequence'].next_by_code('agencies.legal')
        return super(AgenciesLegal, self).create(vals)
    
    
    
    
    