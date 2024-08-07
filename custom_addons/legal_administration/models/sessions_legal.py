from odoo import api, fields, models

class SessionsLegal(models.Model):
    _name = "sessions.legal"
    _description = "Sessions Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'court'
    
    
    court = fields.Char(string='Court', required=True)
    date_and_time_of_session = fields.Datetime(string='Session Date & Time', default=fields.Datetime.now, required=True)
    session_text = fields.Text(string='Session Text', required=True)
    session_attachment = fields.Binary(string='Session Attached', required=True)
    issue = fields.Many2one('issues.legal', string='Issue', required=True)
    active = fields.Boolean(string='Active', default=True)
    appeal_id = fields.Many2one('appeal.legal', string='Appeal', required=True)
    
    @api.onchange('issue')
    def onchange_issue(self):
        self.court = self.issue.court_name
        
    
    