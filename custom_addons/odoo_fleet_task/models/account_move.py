from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_vehicle = fields.Boolean(string='Is Vehicle')

    def action_post(self):
        super(AccountMove, self).action_post()
        for line in self.invoice_line_ids:
            if line.asset_category_id.id == 1:
                self.env['fleet.vehicle'].create({
                    'model_id': line.asset_category_id.model_id.id,
                    'license_plate': line.product_id.name,
                })
                print("=========== Post")

