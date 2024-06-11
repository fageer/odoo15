from odoo import http
from odoo.http import request
from odoo.addons.website_sale_delivery.controllers.main import WebsiteSaleDelivery



class CreateCv(http.Controller):    
    @http.route('/createcv_webform', type='http', auth="user", website=True)
    def createcv_webform(self, **kwargs):
        print('excution==============================================================')
        partner_records = request.env['res.partner'].sudo().search([])
        country_records = request.env['res.country'].sudo().search([])
        city_records = request.env['res.country.state'].sudo().search([])
        job_records = request.env['jobs'].sudo().search([])
        skill_records = request.env['skills.tags'].sudo().search([])
        print(country_records, "================================================================")
        current_partner = request.env.user.partner_id
        return request.render('create_cv.create_cv_23', {
                                                                'partner_records': partner_records,
                                                                'country_records': country_records,
                                                                'city_records': city_records,
                                                                'job_records': job_records,
                                                                'skill_records': skill_records,
                                                                'current_partner': current_partner,
                                                                })



    @http.route('/create/webcv', type='http', auth="public", website=True)
    def create_webcv(self, **kwargs):
        print(kwargs, 'excution==============================================================')
        cv_vals = {
            'image': kwargs.get('image'),
            'name_id': kwargs.get('name_id'),
            'email': kwargs.get('email'),
            'job_title': kwargs.get('job_title'),
            'phone_number': kwargs.get('phone_number'),
            'country_id': kwargs.get('country_id'),
            'city_id': kwargs.get('city_id'),
            'summary': kwargs.get('summary'),
        }
        request.env['create.cv'].sudo().create(cv_vals)
        return request.render('create_cv.cv_thanks', {})
    