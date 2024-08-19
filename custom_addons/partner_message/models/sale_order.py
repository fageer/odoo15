from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        sale_order = super(SaleOrder, self).create(vals)
        partner_id = sale_order.partner_id.id
        partner = self.env['res.partner'].browse(partner_id)
        sale_order_url = f"http://localhost:8066/web#cids=1&menu_id=243&action=398&model=sale.order&view_type=form&id={sale_order.id}"
        partner.message_post(body=f"Quotation [<a href='{sale_order_url}'>{sale_order.name}</a>] Created")
        return sale_order

    def action_cancel(self):
        super(SaleOrder, self).action_cancel()
        partner_id = self.partner_id.id
        partner = self.env['res.partner'].browse(partner_id)
        sale_order_url = f"http://localhost:8066/web#cids=1&menu_id=243&action=398&model=sale.order&view_type=form&id={self.id}"
        partner.message_post(body=f"Quotation [<a href='{sale_order_url}'>{self.name}</a>] Canceled")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        partner_id = self.partner_id.id
        partner = self.env['res.partner'].browse(partner_id)
        sale_order_url = f"http://localhost:8066/web#cids=1&menu_id=243&action=398&model=sale.order&view_type=form&id={self.id}"
        partner.message_post(body=f"Quotation [<a href='{sale_order_url}'>{self.name}</a>] Confirmed")
