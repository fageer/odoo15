from odoo import api, fields, models, _


class SkillsTags(models.Model):
    _name = "skills.tags"
    _description = 'Skills Tags'


    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')


    _sql_constraints = [
        ('unique_tag_name', 'unique (name)', 'Name Already Exists.')
    ]
    