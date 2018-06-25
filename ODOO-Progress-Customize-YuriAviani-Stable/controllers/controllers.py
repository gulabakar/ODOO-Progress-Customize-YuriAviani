# -*- coding: utf-8 -*-
from odoo import http

# class Mytestmodule(http.Controller):
#     @http.route('/mytestmodule/mytestmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mytestmodule/mytestmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mytestmodule.listing', {
#             'root': '/mytestmodule/mytestmodule',
#             'objects': http.request.env['mytestmodule.mytestmodule'].search([]),
#         })

#     @http.route('/mytestmodule/mytestmodule/objects/<model("mytestmodule.mytestmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mytestmodule.object', {
#             'object': obj
#         })