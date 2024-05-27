from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    cash = fields.Boolean(string='Cash')
    postpaid = fields.Boolean(string='Postpaid')
    limit = fields.Float(string='Limit', default='100000')