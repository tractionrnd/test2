# -*- coding: utf-8 -*-
from odoo import models, fields

class ExtCRMLead(models.Model):
	_inherit = 'sale.order'
    
    @api.multi
    def generate_po_from_so(self):
        test = None