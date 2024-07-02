from odoo import http


class LoginApi(http.Controller):
    @http.route("/api/login", methods=["GET"], type="http", auth="public", csrf=False)
    def test_login(self, **kw):
        print("=================================================")
        print("inside test_login method")
        print("inside test_login method")
        print("=================================================")

