# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class PurchaseOrderAdv(models.TransientModel):
    _name = "tcrm_po_from_so.purchase_order_adv"
    _description = "Generate PO from SO"

    partner_id = fields.Many2one('res.partner', string='Customer', required=True, help="You can find a customer by its Name, TIN, Email or Internal Reference.")
    
    @api.multi
    def generate_po(self):
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
        
        poModel = self.env['purchase.order']
        poLineModel = self.env['purchase.order.line']

        sale = sale_orders[0]
        poItem = poModel.create({
            'date_order': sale.confirmation_date,
            'partner_id': sale.partner_id.id
        })

        for line_item in sale.order_line:
            poLineModel.create({
                'order_id': poItem.id,
                'product_id': line_item.product_id.id,
                'product_qty': line_item.product_uom_qty,
                'product_uom': line_item.product_uom.id,
                'date_planned': line_item.create_date,
                'name': line_item.name,
                'price_unit': line_item.price_unit
            })

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'target': 'current',
            'res_id': poItem.id,
            'type': 'ir.actions.act_window' }