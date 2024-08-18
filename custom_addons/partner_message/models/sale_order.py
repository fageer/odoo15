from odoo import api, fields, models


# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
#     def _compute_sale_order_count(self):
#         super(ResPartner, self)._compute_sale_order_count()
#         # self.message_post(body="Sale Order Created")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        sale_order = super(SaleOrder, self).create(vals)
        partner = self.env['res.partner'].browse(vals.get('partner_id'))
        partner.message_post(body="Sale Order Created")
        return sale_order

