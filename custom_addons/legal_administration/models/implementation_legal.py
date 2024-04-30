from odoo import api, fields, models

class ImplementationLegal(models.Model):
    _name = "implementation.legal"
    _description = "Implementation Legal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = ''
    
    
    status = fields.Selection([
        ('new', 'New'),
        ('underway', 'Underway')], string='Status')
    attachments = fields.Binary(string='Attachments')
    type_of_judge = fields.Selection([
        ('primary', 'Primary'),
        ('appellate', 'Appellate')], string='Type Of Judge')
    issue = fields.Many2one('issues.legal', string='Issue', required=True)
    appeal = fields.Char(string='Appeal')
    
    
    
    
    