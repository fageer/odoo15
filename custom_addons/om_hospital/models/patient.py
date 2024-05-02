from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"


    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference', tracking=True, readonly=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default='male')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count', store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    parent = fields.Char(string='Parent')
    marital_status = fields.Selection([
        ('married', 'Married'),
        ('single', 'Single')], string='Marital Status', tracking=True)
    partner_name = fields.Char(string='Partner Name')
    
    
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])


    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > date.today():
                raise ValidationError(_('Date of Birth cannot be in the future.'))

    @api.ondelete(at_uninstall=False)
    def _check_appointment(self):
        for rec in self:
            if rec.appointment_count > 0:
                raise ValidationError(_("You Can't Delete Patient With Appointment !!"))
            
            
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)


    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0


    def name_get(self):
        return [(record.id, f"[{record.ref}] {record.name}") for record in self]

