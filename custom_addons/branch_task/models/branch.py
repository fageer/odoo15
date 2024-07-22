from odoo import api, fields, models, _


class BranchBranch(models.Model):
    _name = "branch.branch"
    _description = "Branches"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(string='Reference', readonly=True)
    name = fields.Char(string='Name', required=True)
    employees_ids = fields.Many2many('res.users', string='Employees')
    responsible_id = fields.Many2one('res.users', string='Responsible')
    location_id = fields.Many2one('stock.location', string='Location', required=True)

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _(f"{self.name} (Copy)")
        return super(BranchBranch, self).copy(default)

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Name Already Exists.'),
    ]

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('branch.branch')
        return super(BranchBranch, self).create(vals)
    
    
    