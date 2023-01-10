# -*- coding: utf-8 -*-
# from odoo import http


# class ModulKedatech(http.Controller):
#     @http.route('/modul_kedatech/modul_kedatech/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modul_kedatech/modul_kedatech/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modul_kedatech.listing', {
#             'root': '/modul_kedatech/modul_kedatech',
#             'objects': http.request.env['modul_kedatech.modul_kedatech'].search([]),
#         })

#     @http.route('/modul_kedatech/modul_kedatech/objects/<model("modul_kedatech.modul_kedatech"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modul_kedatech.object', {
#             'object': obj
#         })
