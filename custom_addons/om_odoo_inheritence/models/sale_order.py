from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')

    def _action_confirm(self):
        super(SaleOrder, self)._action_confirm()
        for order in self:
            for line in order.order_line:
                moves = self.env['stock.move'].search([('sale_line_id', '=', line.id)])
                for move in moves:
                    move.x_field = line.x_field

    def action_confirm(self):
        print("Success !!!!!!!!!!!!!!!!!!")
        super(SaleOrder, self).action_confirm()
        self.confirmed_user_id = self.env.user.id

    def action_cancel(self):
        print("Cancelled !!!!!!!!!!!!!!!!!!")
        super(SaleOrder, self).action_cancel()