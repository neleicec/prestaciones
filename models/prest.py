# -*- coding: utf-8 -*- 

from odoo import models, fields

class prest(models.Model):
	_name='prest'
	name = fields.Many2one('hr.employee', string='Employee', required=True)
	trimestre = fields.Selection(string = 'Selection Trimester', selection=[('trimestre1', 'First Trimester'),('trimestre2','Second Trimester'),('trimestre3','Third Quarter'),('trimestre4','Fourth Trimester')],required=True, help='Indique el trimestre a calcular')
	wage1 = fields.Float('Wage',digits=(16,2), required=True, related='name.wage1',readonly=True, help="Basic Salary of the employee")
#Pendiente por calcular
	wage_day1= fields.Float(string='Salario Diario', digits=(26,2),) 
	alic_util= fields.Float(string='Alicuota de Utilidades', digits=(26,2))
	alic_vac= fields.Float(string='Alicuota de Vacaciones', digits=(26,2))
	sal_int= fields.Float(string='Salario Integral', digits=(26,2))
# #Son fijos
# 	def dias(self):
# 	return 15

class employee(models.Model):
	_inherit='hr.employee'
	wage1 = fields.Float('Wage', digits=(16,2), required=True)
	wage_day1 = fields.Float(string='Salario Diario',digits=(26,2), readonly=True)

# @api.onchange('name')
# def _onchange_employee_id(self):
# 	old_wage=self.employee_id.wage1
# 	old_wage_day=(self.employee_id.wage_day1)/ 30
# 	wage1 = old_wage
# 	wage_day1 = old_wage_day
