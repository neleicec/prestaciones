#  -*- coding: utf-8 -*- 

from odoo import models, fields, api

class presta(models.Model):
	_name='presta'
	name = fields.Many2one('hr.employee', 
		string='Empleado', 
		required=True)