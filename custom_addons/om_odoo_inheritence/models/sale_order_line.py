from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
    x_field = fields.Char('X Field')

    def action_confirm(self):
        print("Success !!!!!!!!!!!!!!!!!!")
        super(SaleOrderLine, self).action_confirm()
        self.confirmed_user_id = self.env.user.id

    def action_cancel(self):
        print("Cancelled !!!!!!!!!!!!!!!!!!")
        super(SaleOrderLine, self).action_cancel()
