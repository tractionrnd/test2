# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ExtMailMassMailingList(models.Model):
    _inherit = 'mail.mass_mailing.list'

    x_dynamicsid = fields.Char(
        string=u'Dynamics ID'
    )