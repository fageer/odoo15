from odoo import api, fields, models

class IssuesLegal(models.Model):
    _name = "issues.legal"
    _description = "Issues Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    
    case_number = fields.Integer(string='Case Number')
    invitation_date = fields.Date(string='Invitation Date')
    court_name = fields.Char(string='Court Name')
    court_type = fields.Selection([
        ('executive', 'Executive'),
        ('resumption', 'Resumption'),
        ('supreme', 'Supreme')], string='Court Type')
    judge = fields.Text(string='Judge')
    claimant = fields.Text(string='Claimant')
    status = fields.Selection([
        ('perspective', 'Perspective'),
        ('finished', 'Finished')], string='Status')
    defendant = fields.Text(string='Defendant')
    # sessions_ids = fields.One2many('sessions.legal', string='Sessions')
    # appeals_ids = fields.One2many('appeals.legal', string='Appeals')
    total_case_fees = fields.Float(string='Total Case Fees')
    judgment_number = fields.Integer(string='Judgment Number')
    ruling_text = fields.Text(string='Ruling Text')
    ruling_date = fields.Date(string='Ruling Date')
    court = fields.Char(string='Court Name')
    judgment_attached = fields.Binary(string='Judgment Attached')
    active = fields.Boolean(string='Active', default=True)
    