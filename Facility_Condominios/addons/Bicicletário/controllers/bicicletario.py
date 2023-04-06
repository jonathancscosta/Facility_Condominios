from odoo import http
from odoo.http import request

class Bicicletario(http.Controller):
    @http.route('/bicicletario/bikes', auth='public')
    def index(self, **kw):
        bikes = request.env['bicicletario.bike'].search([])
        return http.request.render('bicicletario.index', {
            'bikes': bikes,
        })
