from odoo import api, fields, models

class SessionsLegal(models.Model):
    _name = "sessions.legal"
    _description = "Sessions Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'court'
    
    
    court = fields.Char(string='Court')
    date_and_time_of_session = fields.Datetime(string='Session Date & Time', default=fields.Datetime.now)
    # session_requirements = fields.One2many(string='Session Requirements')
    session_text = fields.Text(string='Session Text')
    session_attachment = fields.Binary(string='Session Attached')
    issue = fields.Many2one('issues.legal', string='Issue')
    active = fields.Boolean(string='Active', default=True)
    
    @api.onchange('issue')
    def onchange_issue(self):
        self.court = self.issue.court_name
        
    
    