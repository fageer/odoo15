from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
import base64


class ResPartnerPortal(CustomerPortal):
    @http.route(['/new/partner'], type='http', method=['POST', 'GET'], auth="user", website=True)
    def new_partner(self, **kwargs):
        country_records = request.env['res.country'].sudo().search([])
        state_records = request.env['res.country.state'].sudo().search([])
        vals = {
            'country_records': country_records,
            'state_records': state_records,
            'page_name': 'new_partner',
        }
        if request.httprequest.method == "POST":
            error_list = []
            if not kwargs.get('name'):
                error_list.append("Name field is mandatory ❌!")
            if not error_list:
                file = kwargs.get('image')
                partner_vals = {
                    'image_1920': base64.b64encode(file.read()),
                    'name': kwargs.get('name'),
                    'country_id': int(kwargs.get('country_id')),
                    'state_id': int(kwargs.get('state_id')),
                    'city': kwargs.get('city'),
                    'street': kwargs.get('street'),
                    'street2': kwargs.get('street'),
                    'phone': kwargs.get('phone'),
                    'nationality': kwargs.get('nationality'),
                    'date_of_birth': kwargs.get('date_of_birth'),
                    'birth_address': kwargs.get('birth_address'),
                    'id_number': kwargs.get('id_number'),
                }
                request.env['res.partner'].sudo().create(partner_vals)
                vals['success_msg'] = "Submited Successfully ✔!"
            else:
                vals['error_list'] = error_list

        return request.render('res_partner_portal_task.new_partner_form_view_portal', vals)
