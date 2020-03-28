# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	inventory_valuation = fields.Char(string="Inventory Valuation")
	property_stock_account_input_categ_id = fields.Many2one(
		'account.account', 'Stock Input Account', company_dependent=True,
		domain=[('deprecated', '=', False)], oldname="property_stock_account_input_categ",
		help="When doing real-time inventory valuation, counterpart journal items for all incoming stock moves will be posted in this account, unless "
			 "there is a specific valuation account set on the source location. This is the default value for all products in this category. It "
			 "can also directly be set on each product")
	property_stock_account_output_categ_id = fields.Many2one(
		'account.account', 'Stock Output Account', company_dependent=True,
		domain=[('deprecated', '=', False)], oldname="property_stock_account_output_categ",
		help="When doing real-time inventory valuation, counterpart journal items for all outgoing stock moves will be posted in this account, unless "
			 "there is a specific valuation account set on the destination location. This is the default value for all products in this category. It "
			 "can also directly be set on each product")
	property_stock_valuation_account_id = fields.Many2one(
		'account.account', 'Stock Valuation Account', company_dependent=True,
		domain=[('deprecated', '=', False)],
		help="When real-time inventory valuation is enabled on a product, this account will hold the current value of the products.",)
