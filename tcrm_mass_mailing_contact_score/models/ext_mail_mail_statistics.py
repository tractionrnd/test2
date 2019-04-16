# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ExtMailMailStatistics(models.Model):
    _inherit = 'ext_mail_mail_statistics'

    @api.onchange('sent', 'opened', 'clicked', 'replied', 'bounced')
    def _onchange_total_minbill(self):
        raise ValidationError("Error: %s" % str(self._origin))