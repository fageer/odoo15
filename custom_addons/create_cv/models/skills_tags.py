from odoo import api, fields, models, _


class SkillsTags(models.Model):
    _name = "skills.tags"
    _description = 'Skills Tags'
    _rec_name = 'skill_name'


    skill_name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')


    
    