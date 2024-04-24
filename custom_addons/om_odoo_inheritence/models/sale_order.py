from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    name = fields.Char(string='Nmae', required=True)

    def test_function(self):
        return