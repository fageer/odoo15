from odoo import api, fields, models, _


class Jobs(models.Model):
    _name = "jobs"
    _description = 'Jobs'
    _rec_name = 'job_name'


    job_name = fields.Char(string='Job Name', required=True)
    industry = fields.Char(string='Industry')
