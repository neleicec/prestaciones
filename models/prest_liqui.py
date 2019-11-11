#  -*- coding: utf-8 -*- 

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

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

	@api.multi
	@api.depends('name')
	def _totaltotal(self):
		for record in self:
			sumador_anual = 0.0
			sumador_interes = 0.0
			gs = self.env['prest'].search([])
			for j in gs:
				if j.name == record.name:
					sumador_anual = sumador_anual + j.anual
					sumador_interes = sumador_interes + j.interes
			record.total_total = sumador_anual
			record.total_interes = sumador_interes
				

	total_total = fields.Float(
		string='Total a Liquidar',
		compute='_totaltotal',
		store=True)
	total_interes = fields.Float(
		string="Total Intereses",
		compute="_totaltotal",
		store=True
	)
