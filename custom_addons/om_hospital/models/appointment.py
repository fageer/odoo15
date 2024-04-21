from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'


    patient_id = fields.Many2one('hospital.patient', string='Patient', help='Patient name')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now, help='Time of booking')
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, help='Date of booking')
    ref = fields.Char(string='Reference', tracking=True, default='HP00', help='This is reference to the patient record')
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string='Status', required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref


    def action_test(self):
        print('Clicked Button !!!!!!!')
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Clicked Successfully',
                'type': 'rainbow_man',
            }
        }


    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
    def action_done(self):
        for rec in self:
            rec.state = 'done'
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

