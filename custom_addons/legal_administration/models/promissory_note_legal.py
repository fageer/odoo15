from odoo import api, fields, models


class PromissoryNoteLegal(models.Model):
    _name = "promissory.note.legal"
    _description = "Promissory Note Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'bond_issuer'
    
    bond_issuer = fields.Char(string='Bond Issuer')
    document_status =  fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')], string='Document Status', required=True)
    
    
    
    