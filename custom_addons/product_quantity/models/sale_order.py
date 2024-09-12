from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _action_confirm(self):
        super(SaleOrder, self)._action_confirm()
        for order in self:
            for line in order.order_line:
                if line.product_uom_qty > line.product_id.qty_available:
                    raise ValidationError(_(f'You Don\'t Have Enough Quantity From {line.product_id.name}.'))





