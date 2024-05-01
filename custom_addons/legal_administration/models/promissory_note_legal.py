from odoo import api, fields, models


class PromissoryNoteLegal(models.Model):
    _name = "promissory.note.legal"
    _description = "Promissory Note Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'bond_issuer'
    
    bond_issuer = fields.Char(string='Bond Issuer', compute='_compute_bond_issuer', store=True)
    document_status =  fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')], string='Document Status', required=True)
    
    @api.depends('document_status')
    def _compute_bond_issuer(self):
        for rec in self:
            rec.bond_issuer = self.env.user.company_id.name
        
    
    
    