from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    advertiser_id = fields.Many2one('advertiser.advertiser', string="Advertiser")
    advertisement_type = fields.Many2one('advertisement.type.lines', string="Advertiser Type", domain="[('advertiser_id', '=', advertiser_id)]")

    def action_create_purchase_order(self):
        # Create the Purchase Order
        purchase_order = self.env['purchase.order'].create({
            'partner_id': self.advertiser_id.advertiser_id.id,
            'origin': self.name,
            'order_line': [(0, 0, {
                'product_id': 75,
                'name': self.advertisement_type.advertiser_type,
                'product_uom_qty': 1,
                'price_unit': self.expected_revenue
            })],
        })

    def action_create_quotation(self):
        # Ensure that the partner (customer) is set
        if not self.partner_id:
            raise ValidationError(_("The lead must have a customer before creating a quotation."))

        # Create the Sale Order
        sale_order = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'opportunity_id': self.id,
            'order_line': [(0, 0, {
                'product_id': 75,
                'name': self.name,
                'product_uom_qty': 1,
                'price_unit': self.expected_revenue
            })],
        })

        self.action_create_purchase_order()

        # Optionally, you can perform additional actions like confirming the sale order
        # sale_order.action_confirm()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Quotation',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'res_id': sale_order.id,
            'target': 'current',
        }




