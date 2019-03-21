# -*- coding: utf-8 -*-
from odoo import models, fields

class Dynamics(models.Model):
	_name = 'tcrm_dynamics_integrate.dynamics'
	_description = 'TCG Dynamics'
	_inherit = ['mail.thread']
	
	x_name = fields.Text(
		string=u'Name',
	)
	