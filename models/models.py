# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductCategory(models.Model):
	_inherit = 'product.category'

	property_stock_valuation_account_id = fields.Many2one(
			'account.account', 'Stock Valuation Account', company_dependent=True,
			domain=[('deprecated', '=', False)],
			help="When real-time inventory valuation is enabled on a product, this account will hold the current value of the products.",)