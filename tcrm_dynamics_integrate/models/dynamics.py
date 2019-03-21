# -*- coding: utf-8 -*-
from odoo import models, fields

class Dynamics(models.Model):
	_name = 'tcg.dynamics'
	
	x_name = fields.Text(
		string=u'Name',
	)
	