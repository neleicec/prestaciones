# -*- coding: utf-8 -*- 

from odoo import models, fields, api
# CAMPOS TRIMESTRALES
class prest(models.Model):
	_name='prest'
	name = fields.Many2one('hr.employee', 
		string='Empleado', 
		required=True)
	trimestre = fields.Selection(
		string = 'Seleccione Trimestre', 
		selection=[('trimestre1', 'First Trimester'),('trimestre2','Second Trimester'),('trimestre3','Third Quarter'),('trimestre4','Fourth Trimester')],
		required=True,
		default='trimestre1', 
		help='Indique el trimestre a calcular')
	sueldo = fields.Float(
		string='Sueldo',
		digits=(16,2), 
		required=True, 
		related='name.wage1',
		readonly=True, 
		help="Basic Salary of the employee")
	vac_concepto= fields.Float(
		string='Concepto Vacaciones', 
		required=True, 
		related='name.concepto_vac', 
		readonly=True)
	tasa_t=fields.Float(
		string='Tasa Trimestral',
		required=True)

 	def _dias(self):
		return 15
	dias_sal = fields.Integer(
		string='Dias', 
		default=_dias, 
		readonly=True)

	@api.onchange('name')
	def _saldia(self):
		for record in self:
			record.wage_day1 = record.sueldo / 30
	wage_day1= fields.Float(
		string='Salario Diario', 
		digits=(26,2), 
		compute='_saldia', 
		readonly=True)

	@api.onchange('name')
	def _alic(self):
		for record in self:
			record.alic_util = (((record.sueldo/30) * 30)/360)
	alic_util= fields.Float(
		string='Alicuota Utilidades', 
		digits=(26,2),
		compute='_alic', 
		readonly=True)

	@api.onchange('name')
	def _vac(self):
		for record in self:
			record.alic_vac = ((record.sueldo/30)*(record.vac_concepto) / 360)
	alic_vac= fields.Float(
		string='Alicuota Vacaciones', 
		digits=(26,2), 
		compute=_vac)

	@api.onchange('name')
	def _int(self):
		for record in self:
			record.sal_int = ((record.sueldo/30)+ record.alic_util + record.vac_concepto)
	sal_int= fields.Float(
		string='Salario Integral', 
		digits=(26,2), 
		readonly=True,
		compute='_int')

	@api.onchange('name')
	def _total1(self):
		for record in self:
			record.total_prest1 = (record.sal_int * record.dias_sal)
	total_prest1= fields.Float(
		string='Concepto Prestaciones', 
		readonly=True, 
		compute='_total1')

	@api.onchange('trimestre')
	def _trim(self):
		for record in self:
			if record.trimestre == 'trimestre4':
				record.total_prest2 = (record.sal_int * record.dias_h) 
				record.anual = (record.total_prest1 + record.total_prest2)
	total_prest2= fields.Float(
		string='Concepto Dias Adicionales', 
		readonly=True, 
		compute='_trim')			
	anual= fields.Float(
		string='Anual',
		readonly=True,
		compute='_al_ano')

	# CAMPOS ANUALES 

	@api.onchange('name')
	def _diah(self):
		for record in self:
				if (record.name.years_service) <= 2.0:
					dias_h = 0.0
				else: 
					years_service2 = float(record.name.years_service)
					sumador = years_service2 - 1.0
					sumadorx = sumador * 2.0 
					record.dias_h = sumadorx
					if(record.dias_h) >=30.0:
						record.dias_h=30
	dias_h= fields.Float(
		string='Dias Adicionales', 
		digits=(26,2), 
		readonly=True, 
		compute='_diah')



# Crar campo Wage1 en Empleado

class employee(models.Model):
	_inherit='hr.employee'
	wage1 = fields.Float('Wage', 
		digits=(16,2), 
		required=True)
	concepto_vac = fields.Float(
		string='Concepto Vacaciones', 
		required=True, 
		help="Número de días que le pagan al trabajador por concepto de vacaciones")