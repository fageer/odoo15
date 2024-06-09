from odoo import http
from odoo.http import request
from odoo.addons.website_sale_delivery.controllers.main import WebsiteSaleDelivery



class CreateCv(http.Controller):    
    @http.route('/createcv_webform', type='http', auth="public", website=True)
    def createcv_webform(self, **kwargs):
        print('excution==============================================================')
        partner_records = request.env['res.partner'].sudo().search([])
        country_records = request.env['res.country'].sudo().search([])
        city_records = request.env['res.country.state'].sudo().search([])
        job_records = request.env['jobs'].sudo().search([])
        print(country_records, "================================================================")
        return http.request.render('create_cv.create_cv_23', {
                                                                'partner_records': partner_records,
                                                                'country_records': country_records,
                                                                'city_records': city_records,
                                                                'job_records': job_records,
                                                                })



    @http.route('/create/webcv', type='http', auth="public", website=True)
    def create_webcv(self, **kwargs):
        print(kwargs, 'excution==============================================================')
        # partner_vals = {
        #     'name': kwargs.get('name_id'),
        #     'email': kwargs.get('email'),
        #     'country_id': kwargs.get('country_id'),
        #     'state_id': kwargs.get('city_id'),
        #     'city': kwargs.get('city_id'),
        #     'phone': kwargs.get('phone_number'),
        # }
        # request.env['res.partner'].sudo().create(partner_vals)
        
        request.env['create.cv'].sudo().create(kwargs)
        return request.render('create_cv.cv_thanks', {})
    