from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _order = 'id desc'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference', tracking=True, readonly=True)
    age = fields.Integer(string='Age', compute='_compute_age', inverse='_inverse_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default='male')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    parent = fields.Char(string='Parent')
    marital_status = fields.Selection([
        ('married', 'Married'),
        ('single', 'Single')], string='Marital Status', tracking=True)
    partner_name = fields.Char(string='Partner Name')
    is_birthday = fields.Boolean(string='Is Birthday', compute="_compute_is_birthday")
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')

    @api.depends('date_of_birth')
    def _compute_is_birthday(self):
        for rec in self:
            is_birthday = False
            if rec.date_of_birth:
                today = date.today()
                if today.day == rec.date_of_birth.day and today.month == rec.date_of_birth.month:
                    is_birthday = True
            rec.is_birthday = is_birthday

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    # @api.depends('appointment_ids')
    # def _compute_appointment_count(self):
    #     appointment_group = self.env['hospital.appointment'].read_group(domain=[], fields=['patient_id'],
    #                                                                     groupby=['patient_id'])
    #     for appointment in appointment_group:
    #         patient_id = appointment.get('patient_id')[0]
    #         patient_rec = self.browse(patient_id)
    #         patient_rec.appointment_count = appointment['patient_id_count']
    #         self -= patient_rec
    #     self.appointment_count = 0

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > date.today():
                raise ValidationError(_('Date of Birth cannot be in the future.'))

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

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

    def action_view_appointments(self):
        return {
                'name': 'Appointment',
                'res_model': 'hospital.appointment',
                'view_mode': 'tree,form,calendar,activity',
                'context': {
                            'default_patient_id': self.id,
                            },
                'domain': [('patient_id', '=', self.id)],
                'target': 'current',
                'type': 'ir.actions.act_window',
                }

