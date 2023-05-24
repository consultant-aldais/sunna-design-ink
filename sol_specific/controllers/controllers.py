# -*- coding: utf-8 -*-
# from odoo import http


# class SolSpecific(http.Controller):
#     @http.route('/sol_specific/sol_specific/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sol_specific/sol_specific/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sol_specific.listing', {
#             'root': '/sol_specific/sol_specific',
#             'objects': http.request.env['sol_specific.sol_specific'].search([]),
#         })

#     @http.route('/sol_specific/sol_specific/objects/<model("sol_specific.sol_specific"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sol_specific.object', {
#             'object': obj
#         })
