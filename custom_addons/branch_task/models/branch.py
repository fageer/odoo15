from odoo import api, fields, models, _

class BranchBranch(models.Model):
    _name = "branch.branch"
    _description = "Branches"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    ref = fields.Char(string='Referance', readonly=True)
    name = fields.Char(string='Name', required=True)
    employees_ids = fields.Many2many('res.partner', string='Employees')
    responsible_id = fields.Many2one('res.partner', string='Responsible')
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    
    
    
    
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('branch.branch')
        return super(BranchBranch, self).create(vals)
    
    
    