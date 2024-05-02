from odoo import api, fields, models


class ContractsLegal(models.Model):
    _name = "contracts.legal"
    _description = "Contracts Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = ''
    
    decade_number = fields.Char(string='Decade Number')
    contract_attached = fields.Binary(string='Contract Attached', required=True)
    real_estate = fields.Many2one('product.product', string='Real Estate', required=True)
    beginning_of_decade = fields.Date(string='Beginning of Decade', required=True)
    ending_of_decade = fields.Date(string='Ending of Decade', required=True)
    
    
    @api.model
    def create(self, vals):
        vals['decade_number'] = self.env['ir.sequence'].next_by_code('contracts.legal')
        return super(ContractsLegal, self).create(vals)
    
    
    
    
    