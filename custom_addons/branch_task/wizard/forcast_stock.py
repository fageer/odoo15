import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ForcastStockWizard(models.TransientModel):
    _name = "forcast.stock.wizard"
    _description = 'Forcast Stock Wizard'
    
    
    request_id = fields.Many2one('stock.request', string='Stock Request')
    
    
    @api.onchange('request_id')
    def _onchange_request_id(self):
        self.state = self.request_id.state
        products = self.request_id.product_lines_ids
        for product in products:
            print("context ======================", product.product_id.name)
    
    
    


