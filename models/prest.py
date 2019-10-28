# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class prest(models.Model):
	_name='prest'
	name = fields.Many2one('hr.employee', string='Employee', required=True)
	trimestre = fields.Selection(string = 'Selection Trimester', selection=[('trimestre1', 'First Trimester'),('trimestre2','Second Trimester'),('trimestre3','Third Quarter'),('trimestre4','Fourth Trimester')],required=True, help='Indique el trimestre a calcular')
	wage1 = fields.Float('Wage',digits=(16,2), required=True, related='name.wage1',readonly=True, help="Basic Salary of the employee")
#Pendiente por calcular
	alic_vac= fields.Float(string='Alicuota de Vacaciones', digits=(26,2))
	sal_int= fields.Float(string='Salario Integral', digits=(26,2))
	
#Son fijos
 	def _dias(self):
		return 15
	dias_sal = fields.Integer(string='Dias', default=_dias, readonly=True)

	@api.onchange('name')
	def _saldia(self):
		for record in self:
			record.wage_day1 = record.wage1 / 30
	wage_day1= fields.Float(string='Salario Diario', digits=(26,2), default=_saldia, readonly=True)

	@api.onchange('name')
	def _alic(self):
		for record in self:
			record.alic_util = (((record.wage1/30) * 30)/360)
	alic_util= fields.Float(string='Alicuota de Utilidades', digits=(26,2),default=_alic, readonly=True)
# Crar campo Wage1 en Empleado
class employee(models.Model):
	_inherit='hr.employee'
	wage1 = fields.Float('Wage', digits=(16,2), required=True)