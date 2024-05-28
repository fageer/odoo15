# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    product_id = fields.Many2one('product.product', string='Product', config_parameter='custom_tasks.product_id')
