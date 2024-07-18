from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # def _action_confirm(self):
    #     super(SaleOrder, self)._action_confirm()
    #     for order in self:
    #         for line in order.order_line:
    #             for move_id in line.move_ids:
    #                 move_id.product_img = line.product_img




