from odoo import api, fields, models

class AppealLegal(models.Model):
    _name = "appeal.legal"
    _description = "Appeal Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'judge'
    
    objection_text = fields.Text(string='Objection Text', required=True)
    issue = fields.Many2one('issues.legal', string='Issue', required=True)
    date = fields.Date(string='Date', default=fields.Datetime.now, required=True)
    status = fields.Selection([
        ('perspective', 'Perspective'),
        ('finished', 'Finished')], string='Status', required=True)
    judge = fields.Text(string='Judge', required=True)
    sessions_ids = fields.One2many('sessions.legal', 'issue', string='Sessions')
    judgment_number = fields.Integer(string='Judgment Number')
    ruling_text = fields.Text(string='Ruling Text')
    ruling_date = fields.Date(string='Ruling Date')
    court = fields.Char(string='Court Name')
    judgment_attached = fields.Binary(string='Judgment Attached')
    
    
    @api.onchange('issue')
    def onchange_issue(self):
        self.judge = self.issue.judge
        self.sessions_ids = self.issue.sessions_ids
        self.status = self.issue.status
        self.judgment_number = self.issue.judgment_number
        self.ruling_text = self.issue.ruling_text
        self.ruling_date = self.issue.ruling_date
        self.court = self.issue.court_name
        self.judgment_attached = self.issue.judgment_attached
    
    
    