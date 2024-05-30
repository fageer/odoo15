from odoo import api, fields, models, _

class CreateCv(models.Model):
    _name = "create.cv"
    _description = "Create Cv"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    job_title = fields.Char(string='Job Title')
    phone_number = fields.Char(string='Phone Number')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.city', string='City', domain="[('country_id', '=', country_id)]")
    image = fields.Image(string='Image')
    summary = fields.Html(string='Summary')
    skills_ids = fields.Many2many('skills.tags', string='Skills')
    linkedin = fields.Char(string='linkedIn URL')
    language_ids = fields.Many2many('res.lang', string='Language')
    experience_lines_ids = fields.One2many('experience.lines', 'cv_id', string='Experience Lines')
    education_lines_ids = fields.One2many('education.lines', 'cv_id', string='Education Lines')
    certificate_lines_ids = fields.One2many('certificate.lines', 'cv_id', string='certificate Lines')
    



# Experience Lines
class ExperienceLines(models.Model):
    _name = "experience.lines"
    _description = "Experience Lines"


    # Experience
    company_name = fields.Char(string='Company Name', required=True)
    job_position = fields.Char(string='Job Position')
    experience_start_date = fields.Date(string='From',  tracking=True)
    experience_end_date = fields.Date(string='To', tracking=True)
    experience_summary = fields.Html(string='Experience Summary')
    cv_id = fields.Many2one('create.cv', string='CV')
    
    
    
# Education Lines
class EducationLines(models.Model):
    _name = "education.lines"
    _description = "Education Lines"


    # Education
    university_name = fields.Char(string='University Name', required=True)
    degree = fields.Char(string='Degree')
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
    organization = fields.Char(string='Organization')
    issue_date = fields.Date(string='Issue Date',  tracking=True)
    cv_id = fields.Many2one('create.cv', string='CV')
    
    
    
    

