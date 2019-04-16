# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class PurchaseOrderAdv(models.TransientModel):
    _name = "tcrm_po_from_so.purchase_order_adv"
    _description = ""

    partner_id = fields.Many2one('res.partner', string='Customer', required=True, help="You can find a customer by its Name, TIN, Email or Internal Reference.")
    
    @api.multi
    def generate_po(self):
        dff = None
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))

         raise ValidationError("Error: %s" % sale_orders)