# -*- coding: utf-8 -*-
from odoo import models, fields

class Dynamics(models.Model):
	_name = 'tcrm_dynamics_integrate.dynamics'
	_inherit = ['mail.alias.mixin']
	
	x_name = fields.Text(
		string=u'Name',
	)
	