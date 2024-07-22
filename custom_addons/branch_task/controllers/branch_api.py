import json
from odoo import http
from odoo.http import request


class BranchApi(http.Controller):
    @http.route("/v1/branch/multi", methods=["POST"], type="json", auth="public", csrf=False)
    def post_branch_multi(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        for key, val in vals.items():
            res = request.env['branch.branch'].sudo().create(val)
            print(res)

    @http.route("/v1/branch/one", methods=["POST"], type="json", auth="public", csrf=False)
    def post_branch_one(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        print(vals)
        try:
            res = request.env['branch.branch'].sudo().create(vals)
            if res:
                print("ID=", res.id)
                print("Ref=", res.ref)
        except Exception as error:
            print("ERROR", error)
