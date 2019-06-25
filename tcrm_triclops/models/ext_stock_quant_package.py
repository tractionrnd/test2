# -*- coding: utf-8 -*-
from odoo import models, fields, api
import json
import requests
from odoo.exceptions import ValidationError

class ExtStockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    @api.multi
    def get_weight(self):

        webserverUrl = self.env['ir.config_parameter'].sudo().get_param('tcrm_triclops.x_tricolops_webserverl') or 'http://localhost:8080/data'
        response = requests.get(webserverUrl)

        if response.status_code == 200:
            jsonResponse = response.json()

            if jsonResponse['status'] != 7:
                raise ValidationError(jsonResponse['message'])

            package_type = self.env['product.packaging'].create({
                'name': self.name,
                'package_carrier_type': 'none',
                'height': jsonResponse['height'],
                'width': jsonResponse['width'],
                'length': jsonResponse['length'],
                'max_weight': jsonResponse['weight']#,
                #'barcode': 'barcode',
                #'shipper_package_code': 'package code'
            })

            self.packaging_id = package_type.id
            self.shipping_weight = jsonResponse['weight']
        else:
            raise ValidationError('Server not responded')