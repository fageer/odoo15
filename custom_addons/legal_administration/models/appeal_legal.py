from odoo import api, fields, models

class AppealLegal(models.Model):
    _name = "appeal.legal"
    _description = "Appeal Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'judge'
    
    objection_text = fields.Text(string='Objection Text')
    issue = fields.Many2one('issues.legal', string='Issue')
    date = fields.Date(string='Date', default=fields.Datetime.now)
    status = fields.Selection([
        ('perspective', 'Perspective'),
        ('finished', 'Finished')], string='Status')
    judge = fields.Text(string='Judge')
    sessions_ids = fields.One2many('sessions.legal', 'issue', string='Sessions')
    judgment_number = fields.Integer(string='Judgment Number')
    ruling_text = fields.Text(string='Ruling Text')
    ruling_date = fields.Date(string='Ruling Date')
    court = fields.Char(string='Court Name')
    judgment_attached = fields.Binary(string='Judgment Attached')
    
    
    @api.onchange('issue')
    def onchange_patient_id(self):
        self.judge = self.issue.judge
        self.sessions_ids = self.issue.sessions_ids
    
    
    