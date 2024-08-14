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

    # Create Branch Using ORM Method
    @http.route("/v1/branch/one/orm", methods=["POST"], type="json", auth="public", csrf=False)
    def post_branch_one_orm(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        try:
            res = request.env['branch.branch'].sudo().create(vals)
            if res:
                return {'message': 'Branch Created Successfully',
                        'id': res.id,
                        'name': res.name}
        except Exception as error:
            return {'error': error}

    # Create Branch Using SQL Query
    @http.route("/v1/branch/one/query", methods=["POST"], type="json", auth="public", csrf=False)
    def post_branch_one_sql(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        try:
            cr = request.env.cr
            columns = ", ".join(vals.keys())
            values = ", ".join(['%s'] * len(vals))
            query = f"""
                INSERT INTO branch_branch ({columns})
                VALUES ({values})
                RETURNING id, name;
            """
            cr.execute(query, tuple(vals.values()))
            res = cr.fetchone()
            print(res)
            if res:
                return {'message': 'Branch Created Successfully',
                        'id': res[0],
                        'name': res[1]}
        except Exception as error:
            return {'error': error}

    @http.route("/v1/branch/<int:branch_id>", methods=["PUT"], type="json", auth="public", csrf=False)
    def update_branch(self, **kw):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        try:
            request.env['branch.branch'].browse(kw.get('branch_id')).write(vals)
            return {'message': 'Branch Updated Successfully'}
        except Exception as error:
            return {'error': error}
