# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ExtStockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def mark_all_done(self):
        for line_item in self.move_line_ids:
            if not line_item.result_package_id:
                line_item.qty_done = line_item.product_uom_qty