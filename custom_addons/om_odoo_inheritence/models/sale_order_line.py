from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
    x_field = fields.Char('X Field')

    @api.multi
    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        # I am assuming field name in both sale.order.line and in stock.move are same and called 'YourField'
        res.update({'x_field': self.x_field})
        return res

    def action_confirm(self):
        print("Success !!!!!!!!!!!!!!!!!!")
        super(SaleOrderLine, self).action_confirm()
        self.confirmed_user_id = self.env.user.id

    def action_cancel(self):
        print("Cancelled !!!!!!!!!!!!!!!!!!")
        super(SaleOrderLine, self).action_cancel()
