from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = ['stock.picking']

    country_id = fields.Many2one('res.country', string="Country", compute='_compute_country_id')
    city_id = fields.Many2one('res.city', string="City", compute='_compute_country_id')
    
    
    @api.depends('group_id')
    def _compute_country_id(self):
        for record in self:
            record.country_id = record.group_id.sale_id.country_id.id
            record.city_id = record.group_id.sale_id.city_id.id
    
    
    