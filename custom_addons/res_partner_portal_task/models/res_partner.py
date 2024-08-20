from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    nationality = fields.Char(string="Nationality")
    date_of_birth = fields.Date(string="Date Of Birth")
    birth_address = fields.Char(string="Birth ِAddress")
    id_number = fields.Char(string="ID number")
    relationship = fields.Char(string="Relationship")
