# -*- coding: utf-8 -*-
from odoo import http

# class VitSoNotif(http.Controller):
#     @http.route('/vit_so_notif/vit_so_notif/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_so_notif/vit_so_notif/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_so_notif.listing', {
#             'root': '/vit_so_notif/vit_so_notif',
#             'objects': http.request.env['vit_so_notif.vit_so_notif'].search([]),
#         })

#     @http.route('/vit_so_notif/vit_so_notif/objects/<model("vit_so_notif.vit_so_notif"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_so_notif.object', {
#             'object': obj
#         })