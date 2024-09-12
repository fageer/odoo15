from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def action_product_quantity(self):
        return {
            'name': _('Product Quantity'),
            'type': 'ir.actions.act_window',
            'res_model': 'stock.quant',
            'view_mode': 'tree',
            'view_id': self.env.ref('product_quantity.stock_quant_tree_wizard_view').id,
            'target': 'new',
            'domain': [('product_id', '=', self.product_id.id)]
        }
