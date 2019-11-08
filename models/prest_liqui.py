#  -*- coding: utf-8 -*- 

from odoo import models, fields, api

class presta(models.Model):
	_name='presta'
	# Barra de empleados
	name = fields.Many2one('hr.employee', 
		string='Empleado', 
		required=True)
	# Muestra la Fecha de Ingreso
	fecha_ing = fields.Date( 
		string='Fecha de Ingreso', 
		required=True,
		related="name.date_in",
		readonly=True)
	# Selecciona la Fecha Actual
	fecha_actual = fields.Date(
		string='Fecha Actual',
		required=True)
		# 
		# 
		# 
		# 
		# 
		# 
	prueba = fields.Char(
		string='prueba',
		compute='_totaltotal')
	

	@api.multi
	def _totaltotal(self):
		for record in self:
			if (record.name.id)== record.prest.name.id:
				record.prueba= "funciona"