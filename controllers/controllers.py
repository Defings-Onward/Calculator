from odoo import http
from odoo.http import request, route

class OwlPlayground(http.Controller):
    @http.route(['/calculator'], type='http', auth='public')
    def show_playground(self):
        """
        Renders the owl playground page
        """
        return request.render('odoo_calculator.playground')
