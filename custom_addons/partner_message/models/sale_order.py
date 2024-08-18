from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        sale_order = super(SaleOrder, self).create(vals)
        partner = self.env['res.partner'].browse(vals.get('partner_id'))
        partner.message_post(body="New Quotation Created")
        return sale_order

    def action_quotation_sent(self):
        super(SaleOrder, self).action_quotation_sent()
        partner_id = self.partner_id.id
        partner = self.env['res.partner'].browse(partner_id)
        partner.message_post(body="Quotation Sent")

    def action_cancel(self):
        super(SaleOrder, self).action_cancel()
        partner_id = self.partner_id.id
        partner = self.env['res.partner'].browse(partner_id)
        partner.message_post(body=f"Quotation [{self.name}] Canceled")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        partner_id = self.partner_id.id
        partner = self.env['res.partner'].browse(partner_id)
        partner.message_post(body=f"Quotation [{self.name}] Confirmed")