from odoo import api, fields, models, _

class CreateCv(models.Model):
    _name = "create.cv"
    _description = "Create Cv"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'


    image = fields.Image(string='Image')
    name_id = fields.Many2one('res.partner', string='Name', required=True, default=lambda self: self.env.user.partner_id.id)
    ref = fields.Char(string='Reference', readonly=True)
    email = fields.Char(string='Email')
    job_title = fields.Many2one('jobs', required=True, string='Job Title')
    phone_number = fields.Char(string='Phone Number')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City', domain="[('country_id', '=', country_id)]")
    linkedin = fields.Char(string='linkedIn URL')
    website = fields.Char(string='Website')
    github = fields.Char(string='Github')
    summary = fields.Html(required=True, string='Summary')
    skills_ids = fields.Many2many('skills.tags', string='Skills')
    language_ids = fields.Many2many('res.lang', string='Language')
    experience_lines_ids = fields.One2many('experience.lines', 'cv_id', string='Experience Lines')
    education_lines_ids = fields.One2many('education.lines', 'cv_id', string='Education Lines')
    certificate_lines_ids = fields.One2many('certificate.lines', 'cv_id', string='Certificate Lines')
    
    
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('create.cv')
        return super(CreateCv, self).create(vals)
    
    
    @api.onchange('name_id')
    def _onchange_name_id(self):
        self.country_id = self.name_id.country_id.id
        self.email = self.name_id.email
        self.phone_number = self.name_id.phone
        self.image = self.name_id.image_1920
        if self.name_id.website:
            self.website = self.name_id.website    
    



# Experience Lines
class ExperienceLines(models.Model):
    _name = "experience.lines"
    _description = "Experience Lines"


    # Experience
    company_name = fields.Char(string='Company Name', required=True)
    job_position = fields.Many2one('jobs', string='Job Position')
    experience_start_date = fields.Date(string='From',  tracking=True)
    experience_end_date = fields.Date(string='To', tracking=True)
    experience_summary = fields.Html(string='Experience Summary')
    cv_id = fields.Many2one('create.cv', string='CV')
    
    
    
# Education Lines
class EducationLines(models.Model):
    _name = "education.lines"
    _description = "Education Lines"


    # Education
    university_name = fields.Many2one('universities', string='University Name', required=True)
    degree = fields.Many2one('degrees', string='Degree')
    education_start_date = fields.Date(string='From',  tracking=True)
    education_end_date = fields.Date(string='To', tracking=True)
    education_summary = fields.Html(string='Education Summary')
    cv_id = fields.Many2one('create.cv', string='CV')
    
    
    
# Certificate Lines
class CertificateLines(models.Model):
    _name = "certificate.lines"
    _description = "Certificate Lines"


    # Certificate
    name = fields.Char(string='Certificate Name', required=True)
    organization = fields.Many2one('universities', string='Organization')
    degree = fields.Many2one('degrees', string='Degree')
    issue_date = fields.Date(string='Issue Date',  tracking=True)
    cv_id = fields.Many2one('create.cv', string='CV')
    
    
    
    

