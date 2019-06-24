# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ExtStockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    @api.multi
    def get_weight(self):
        #self.packaging_id = 
        self.shipping_weight = 10