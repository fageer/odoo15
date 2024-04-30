from odoo import api, fields, models

class ImplementationLegal(models.Model):
    _name = "implementation.legal"
    _description = "Implementation Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = ''
    
    
    status = fields.Selection([
        ('new', 'New'),
        ('underway', 'Underway')], string='Status', required=True)
    attachments = fields.Binary(string='Attachments', required=True)
    type_of_judge = fields.Selection([
        ('primary', 'Primary'),
        ('appellate', 'Appellate')], string='Type Of Judge', required=True)
    issue = fields.Many2one('issues.legal', string='Issue', required=True)
    appeal = fields.Char(string='Appeal', required=True)
    
    
    
    
    