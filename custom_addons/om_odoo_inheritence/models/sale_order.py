from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _action_confirm(self):
        super(SaleOrder, self)._action_confirm()
        for order in self:
            for line in order.order_line:
                moves = self.env['stock.move'].search([('sale_line_id', '=', line.id)])
                for move in moves:
                    move.x_field = line.x_field
