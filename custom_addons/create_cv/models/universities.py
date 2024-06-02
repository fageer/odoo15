from odoo import api, fields, models, _


class universities(models.Model):
    _name = "universities"
    _description = 'Universities'
    _rec_name = 'university_name'


    university_name = fields.Char(string='University Name', required=True)
    code = fields.Char(string='Code')
    country = fields.Char(string='Country')
    website = fields.Char(string='Website')


    
    