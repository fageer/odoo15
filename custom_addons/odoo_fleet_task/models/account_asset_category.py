from odoo import api, fields, models


class AccountAssetCategory(models.Model):
    _inherit = 'account.asset.category'

    model_id = fields.Many2one('fleet.vehicle.model', string='Model')


