# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ExtMailMassMailingContact(models.Model):
    _inherit = 'mail.mass_mailing.contact'

    x_dynamicssource = fields.Char(
        string=u'Dynamics Source'
    )
    x_dynamicstype = fields.Char(
        string=u'Dynamics Type'
    )
    x_score = fields.Integer(
        string=u'Score'
    )
    x_firstname = fields.Char(
        string=u'First Name'
    )
    x_lastname = fields.Char(
        string=u'Last Name'
    )
    x_title = fields.Char(
        string=u'Job Title'
    )
    
    @api.multi
    def set_score(self, env, model, record, log, score):
        logStr = 'set_score for record ' + str(record.id) + '\n'

        env['mail.mass_mailing.contact'].browse(record.id).write({
            'x_score': score
        })

        log(logStr)

    @api.multi
    def add_score(self, env, model, record, log, score):
        logStr = 'add_score for record ' + str(record.id) + '\n'

        env['mail.mass_mailing.contact'].browse(record.id).write({
            'x_score': record.x_score + score
        })

        log(logStr)