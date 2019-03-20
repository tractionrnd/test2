# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class ExtResPartner(models.Model):
	_inherit = 'res.partner'

	x_dynamics_id = fields.Text(
		string=u'Dyncamics ID',
	)
	