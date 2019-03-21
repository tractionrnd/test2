# -*- coding: utf-8 -*-
from odoo import models, fields

class ExtMailMessage(models.Model):
    _inherit = 'mail.message'

    def parse_body(self, body):
        fields = ['Entity', 'id', 'FirstName','LastName','CompanyName','Email','Phone','Mobile','JobTitle']
        pre_dict={}
        for line in body.split('\n'):
            for field in fields:
                if field in line:
                    split_line=line.split(':')
                    if len(split_line)>1:
                        pre_dict[field]=line.split(':')[1]
        return  pre_dict

    def process_tcg_dynamics_email(self, env, model, record, log):
        if record.model == 'tcrm_dynamics_integrate.dynamics':
            body = record.body
            _dict = self.parse_body(body)

            log(str(_dict))

            #leadModel = env['crm.lead']
            #partnerModel = env['res.partner']
            #lead = leadModel.search([('x_dynamics_id', '=', self.id)])           