from odoo import api, fields, models

class IssuesLegal(models.Model):
    _name = "issues.legal"
    _description = "Issues Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'case_number'

    
    case_number = fields.Char(string='Case Number')
    invitation_date = fields.Date(string='Invitation Date', required=True)
    court_name = fields.Char(string='Court Name', required=True)
    court_type = fields.Selection([
        ('executive', 'Executive'),
        ('resumption', 'Resumption'),
        ('supreme', 'Supreme')], string='Court Type', required=True)
    judge = fields.Text(string='Judge', required=True)
    claimant = fields.Text(string='Claimant', required=True)
    status = fields.Selection([
        ('perspective', 'Perspective'),
        ('finished', 'Finished')], string='Status', required=True)
    defendant = fields.Text(string='Defendant', required=True)
    sessions_ids = fields.One2many('sessions.legal', 'issue', string='Sessions', required=True)
    # appeals_ids = fields.One2many('appeal.legal','issue', string='Appeals', required=True)
    total_case_fees = fields.Float(string='Total Case Fees', required=True)
    judgment_number = fields.Integer(string='Judgment Number')
    ruling_text = fields.Text(string='Ruling Text')
    ruling_date = fields.Date(string='Ruling Date')
    court = fields.Char(string='Court Name')
    judgment_attached = fields.Binary(string='Judgment Attached')
    active = fields.Boolean(string='Active', default=True)
    sessions_count = fields.Integer(string='Sessions Count', compute='_compute_sessions_count')
    
    
    def _compute_sessions_count(self):
        for record in self:
            record.sessions_count = self.env['sessions.legal'].search_count([('id', '=', record.sessions_ids.ids)])
    
    
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
        
        
    def action_open_sessions(self):
        print(self.sessions_ids.ids)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sessions',
            'res_model': 'sessions.legal',
            'domain': [('id', '=', self.sessions_ids.ids)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
        
    