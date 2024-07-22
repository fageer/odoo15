import json
from odoo import http
from odoo.http import request


class BranchApi(http.Controller):
    @http.route("/v1/branch/multi", methods=["POST"], type="json", auth="public", csrf=False)
    def post_branch_multi(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        for key, val in vals.items():
            request.env['branch.branch'].sudo().create(val)
        return {'message': 'Branches Created Successfully'}

    @http.route("/v1/branch/one", methods=["POST"], type="json", auth="public", csrf=False)
    def post_branch_one(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        try:
            request.env['branch.branch'].sudo().create(vals)
            return {'message': 'Branch Created Successfully'}
        except Exception as error:
            print("ERROR", error)

    @http.route("/v1/branch/<int:branch_id>", methods=["PUT"], type="json", auth="public", csrf=False)
    def update_branch(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        # print(vals)
        # try:
        branch = request.env['branch.branch'].browse(kw.get('branch_id')).write(vals)
        print(branch.name)
        # except Exception as error:
        #     print("ERROR: ", error)
