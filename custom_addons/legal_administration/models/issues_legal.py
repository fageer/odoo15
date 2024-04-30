from odoo import api, fields, models

class IssuesLegal(models.Model):
    _name = "issues.legal"
    _description = "Issues Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'case_number'

    
    case_number = fields.Char(string='Case Number')
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
    sessions_ids = fields.One2many('sessions.legal', 'issue', string='Sessions')
    appeals_ids = fields.One2many('appeal.legal','issue', string='Appeals')
    total_case_fees = fields.Float(string='Total Case Fees')
    judgment_number = fields.Integer(string='Judgment Number')
    ruling_text = fields.Text(string='Ruling Text')
    ruling_date = fields.Date(string='Ruling Date')
    court = fields.Char(string='Court Name')
    judgment_attached = fields.Binary(string='Judgment Attached')
    active = fields.Boolean(string='Active', default=True)
    
    
    @api.model
    def create(self, vals):
        vals['case_number'] = self.env['ir.sequence'].next_by_code('issues.legal')
        return super(IssuesLegal, self).create(vals)
    
    
    @api.onchange('court_name')
    def onchange_court_name(self):
        self.court = self.court_name
        
        
    @api.onchange('case_number')
    def onchange_case_number(self):
        self.judgment_number = self.case_number
        
    