from odoo import api, fields, models, _


class Degrees(models.Model):
    _name = "degrees"
    _description = 'Degrees'


    name = fields.Char(string='Degree Name', required=True)
