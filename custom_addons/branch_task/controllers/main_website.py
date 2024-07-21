from odoo import http
from odoo.http import request


class Sale(http.Controller):
    # type ="http","json"
    # auth="public","users","none"
    @http.route('/my_sale_details', type="http", auth="public", website=True)
    def get_sale_orders(self, **kwargs):
        sale_details = request.env['sale.order'].sudo().search([])
        return request.render('branch_task.sale_details_page', {'my_details': sale_details})

    @http.route('/branch_request_submit', type="http", auth="public", website=True, csrf=True)
    def request_branch_submit(self, **kwargs):
        vals = {
            'name': kwargs.get('branch_name'),
            "employees_ids": [[6, 0, [6]]],
            "responsible_id": 2,
            "location_id": 18
        }
        request.env['branch.branch'].sudo().create(vals)
        return request.redirect('/success_page')
