from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')

    def _action_confirm(self):
        super(SaleOrder, self)._action_confirm()
        for order in self:
            for line in order.order_line:
                for move_id in line.move_ids:
                    move_id.x_field = line.x_field
