# -*- coding: utf-8 -*- 

from odoo import models, fields

class prestaciones(models.Model):
	_name='prestaciones'
	name = fields.Many2one('hr.employee', string='Employee', required=True)
	trimestre = fields.Selection(string = 'Selection Trimester', selection=[('trimestre1', 'First Trimester'),('trimestre2','Second Trimester'),('trimestre3','Third Quarter'),('trimestre4','Fourth Trimester')],required=True, help='Indique el trimestre a calcular')
	wage1 = fields.Float('Wage',digits=(16,2), required=True, related='name.wage1',readonly=True, help="Basic Salary of the employee")
	wage_day1= fields.Float(string='Salario Diario', digits=(26,2))

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
