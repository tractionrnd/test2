# -*- coding: utf-8 -*-
from odoo import models, fields

class ExtCRMLead(models.Model):
	_inherit = 'crm.lead'

	x_dynamics_id = fields.Text(string=u'Dyncamics ID')
