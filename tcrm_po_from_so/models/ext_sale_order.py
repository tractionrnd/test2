# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ExtCRMLead(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def generate_po_from_so(self):
        poModel = self.env['purchase.order']

        poItem = poModel.create({
            'date_order': self.confirmation_date,
            'partner_id': self.partner_id
        })

        #order_line
        #order_line
        poLineModel = self.env['purchase.order.line']
        for line_item in self.order_line:
            poLineModel.cereate({
                'order_id': poItem.id,
                'product_id': line_item.product_id,
                'product_qty': line_item.product_uom_qty,
                'product_uom': line_item.product_uom,
                'date_planned': line_item.create_date
            })

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'target': 'current',
            'res_id': poItem.id,
            'type': 'ir.actions.act_window' }
