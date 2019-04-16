# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class PurchaseOrderAdv(models.TransientModel):
    _name = "tcrm_po_from_so.purchase_order_adv"
    _description = ""

    @api.multi
    def generate_po(self):
        dff = None