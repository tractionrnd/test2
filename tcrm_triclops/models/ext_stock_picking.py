# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ExtStockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def mark_all_done(self):
        poModel = self.env['purchase.order']