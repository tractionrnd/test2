# -*- coding: utf-8 -*-
from odoo import models, fields
import re

class ExtMailMessage(models.Model):
    _inherit = 'mail.message'

    def parse_body(self, body):
        fields = ['Entity', 'ID', 'FirstName','LastName','CompanyName','Email','Phone','Mobile','JobTitle']
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
            
            brRe = re.compile('<\s*br\s*\/?>')
            bodyClean = re.sub(brRe, '\n', record.body)
            
            #log(bodyClean)

            cleanRe = re.compile('<.*?>')
            bodyClean = re.sub(cleanRe, '', bodyClean)
            bodyClean = bodyClean.replace(u'\xa0', u' ') #common issue in python
            log(bodyClean)

            _dict = ExtMailMessage.parse_body(self, bodyClean)

            #log(str(_dict))

            leadModel = env['crm.lead']
            lead = leadModel.search([('x_dynamics_id', '=', _dict['ID'])])
            if lead:
                log('Found Lead - Updating: ' + str(lead))
                lead.write({'email_from': _dict['Email'], 'phone': _dict['Phone'], 'contact_name': _dict['FirstName'] + ' ' + _dict['LastName'], 'function': _dict['JobTitle'], 'mobile': _dict['Mobile']})
            else:
                partnerModel = env['res.partner']
                partner = partnerModel.search([('x_dynamics_id', '=', _dict['ID'])])
                if partner:
                    log('Found Partner - Updating: ' + str(partner))
                    partner.write({'email': _dict['Email'], 'phone': _dict['Phone'], 'name': _dict['FirstName'] + ' ' + _dict['LastName'], 'function': _dict['JobTitle'], 'mobile': _dict['Mobile']})
                else:
                    log('Create New Lead')
                    leadModel.create({'name': 'Update via Email', 'x_dynamics_id': _dict['ID'], 'email_from': _dict['Email'], 'phone': _dict['Phone'], 'contact_name': _dict['FirstName'] + ' ' + _dict['LastName'], 'function': _dict['JobTitle'], 'mobile': _dict['Mobile']})