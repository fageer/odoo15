import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class StockQuantInherit(models.Model):
    _inherit = ['stock.quant']
    
    def action_fill_loc(self):
        pro = self.env['product.lines'].search([('product_id', '=', self.product_id.id)])
        pro.stock_location_id = self.location_id.id
    
    
    
    
    
    
    
    # name = fields.Char(string='Name')
    # product_id = fields.Many2one('product.product', string='Product')
    # pro_location_info_ids = fields.Many2many('stock.quant', string='Location')
    
    
    # @api.model
    # def default_get(self, fields):
    #     # self.pro_location_info_ids.inventory_quantity
    #     res = super(ForcastStockWizard, self).default_get(fields)
    #     product_id = self.env.context.get('product_id')
    #     if product_id:
    #         res['product_id'] = product_id
    #     return res
    
    # @api.onchange('product_id')
    # def _onchange_product_id(self):
    #     for record in self:
    #         record.name = record.product_id.name
    #         pros = self.env['stock.quant'].search([('product_id', '=', record.product_id.id)])
    #         record.pro_location_info_ids = [(6, 0, pros.ids)]
            
            
            
            
    
    # def add_location(self):
    #     locations = self.pro_location_info_ids
    #     pro_lines = self.env['product.lines'].search('product_id', '=', locations.product_id.id)
    #     for pro in pro_lines:
    #         pro.stock_location_id = locations.location_id.id
    #         pro.stock_location_id = self.pro_location_info_ids.location_id.id
        
    
    
    


