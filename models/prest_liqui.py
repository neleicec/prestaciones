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
	
	@api.multi
	@api.onchange('name')
	def _totaltotal (self):
		for record in self:
			lista_anual = [self.env['prest'].anual]
			lista_id = [self.env['prest'].name.id]
			for i in (lista_id):
				if record.name.id == self.env['prest'].name.id:
					record.total_total = record.total_total + lista_anual[i]
	total_total = fields.Integer(
		string='Total a Liquidar',
		compute='_totaltotal')
