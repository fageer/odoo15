from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')


    def action_confirm(self):
        print("Success !!!!!!!!!!!!!!!!!!")
        super(SaleOrder, self).action_confirm()
        self.confirmed_user_id = self.env.user.id

    def action_cancel(self):
        print("Cancelled !!!!!!!!!!!!!!!!!!")
        super(SaleOrder, self).action_cancel()