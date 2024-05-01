from odoo import api, fields, models


class InvestigationLegal(models.Model):
    _name = "investigation.legal"
    _description = "Investigation Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = ''
    
    document_status =  fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')], string='Document Status', required=True)
    
    
    
    
    