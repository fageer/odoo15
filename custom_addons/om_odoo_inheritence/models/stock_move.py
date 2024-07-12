from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    x_field = fields.Char('X Field')
