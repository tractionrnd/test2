# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ExtStockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    @api.multi
    def get_wieght(self):
        #self.packaging_id = 
        #self.weight = 10
        #self.shipping_weight = 10

        self.write({
            weight: 10,
            shipping_weight: 10
        })