# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ExtStockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    @api.multi
    def get_weight(self):

        package_type = self.env['product.packaging'].create({
            'name': 'Test Name',
            'package_carrier_type': 'none',
            'height': 0,
            'width': 0,
            'length': 1,
            'max_weight': 1.00,
            'barcode': 'barcode',
            'shipper_package_code': 'package code'
        })

        self.packaging_id = package_type.id
        self.shipping_weight = 10