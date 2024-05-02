from odoo import api, fields, models, _

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
    claimant = fields.Char(string='Claimant', required=False)
    claimant_id = fields.Many2one('res.partner', string='Claimant', required=True)
    move_id = fields.Many2one('account.move', 'Invoice' )
    status = fields.Selection([
        ('perspective', 'Perspective'),
        ('finished', 'Finished')], string='Status', required=True)
    defendant = fields.Text(string='Defendant', required=True)
    sessions_ids = fields.One2many('sessions.legal', 'issue', string='Sessions', required=True)
    appeals_ids = fields.One2many('appeal.legal','issue', string='Appeals', required=True)
    total_case_fees = fields.Float(string='Total Case Fees', required=True)
    judgment_number = fields.Integer(string='Judgment Number')
    ruling_text = fields.Text(string='Ruling Text')
    ruling_date = fields.Date(string='Ruling Date')
    court = fields.Char(string='Court Name')
    judgment_attached = fields.Binary(string='Judgment Attached')
    active = fields.Boolean(string='Active', default=True)
    sessions_count = fields.Integer(string='Sessions Count', compute='_compute_sessions_count')
    appeal_count = fields.Integer(string='Appeal Count', compute='_compute_appeal_count')

    def create_invoice(self):
        """ Create a sample invoice """
        invoice = self.env['account.move'].with_context(default_move_type='out_invoice').create({
            'move_type': 'out_invoice',
            'partner_id': self.claimant_id.id,
            'currency_id': self.env.company.currency_id.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [(0, 0, {
                'product_id': 2,
                'quantity': 1,
                'price_unit': self.total_case_fees,
            })],
        })
        self.move_id = invoice.id
        invoice.action_post()

        return invoice
    
    
    def _compute_sessions_count(self):
        for record in self:
            record.sessions_count = self.env['sessions.legal'].search_count([('id', '=', record.sessions_ids.ids)])
            
            
    def _compute_appeal_count(self):
        for record in self:
            record.appeal_count = self.env['appeal.legal'].search_count([('id', '=', record.appeals_ids.ids)])
    
    
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
    def action_open_appeal(self):
        print(self.sessions_ids.ids)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appeals',
            'res_model': 'appeal.legal',
            'domain': [('id', '=', self.appeals_ids.ids)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
        
    