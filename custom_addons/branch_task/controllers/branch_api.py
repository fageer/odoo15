import json
from odoo import http
from odoo.http import request


class BranchApi(http.Controller):
    @http.route("/v1/branch", methods=["POST"], type="json", auth="public", csrf=False)
    def post_branch(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        for key, val in vals.items():
            res = request.env['branch.branch'].sudo().create(val)
            print(res)
        print("=================================================")
        print("inside post_branch method")
        print("inside post_branch method")
        print("=================================================")
