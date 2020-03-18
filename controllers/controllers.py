# -*- coding: utf-8 -*-
from odoo import http

# class VitProductStockValuationAccount(http.Controller):
#     @http.route('/vit_product_stock_valuation_account/vit_product_stock_valuation_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_product_stock_valuation_account/vit_product_stock_valuation_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_product_stock_valuation_account.listing', {
#             'root': '/vit_product_stock_valuation_account/vit_product_stock_valuation_account',
#             'objects': http.request.env['vit_product_stock_valuation_account.vit_product_stock_valuation_account'].search([]),
#         })

#     @http.route('/vit_product_stock_valuation_account/vit_product_stock_valuation_account/objects/<model("vit_product_stock_valuation_account.vit_product_stock_valuation_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_product_stock_valuation_account.object', {
#             'object': obj
#         })