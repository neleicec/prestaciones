# -*- coding: utf-8 -*- 

from odoo import models, fields


class employee(models.Model):
	_inherit='hr.employee'
	wage1 = fields.Float('Wage', digits=(16,2), required=True)
	wage_day1 = fields.Float(string='Salario Diario',digits=(26,2), readonly=True)

