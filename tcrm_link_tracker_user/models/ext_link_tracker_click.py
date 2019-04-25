# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ExtLinkTrackerClick(models.Model):
    _inherit = 'link.tracker.click'

    x_user_name = fields.Char(
        string=u'User Name',
    )

    x_user_email = fields.Char(
        string=u'User Email',
    )

    @api.model
    def add_click(self, code, ip, country_code, stat_id=False):
        self = self.sudo()
        code_rec = self.env['link.tracker.code'].search([('code', '=', code)])

        if not code_rec:
            return None

        again = self.search_count([('link_id', '=', code_rec.link_id.id), ('ip', '=', ip)])

        if not again:
            uname = ''
            uemail = ''
            if self.env.user:
                uname = self.env.user.name
            if self.env.user:
                uemail = self.env.user.email

            data = dict(
                    code=code,
                    ip=ip,
                    country_code=country_code,
                    stat_id=stat_id,
                    x_user_name=uname,
                    x_user_email=uemail,
                )
            self.create(
                super(ExtLinkTrackerClick, self)._get_click_values_from_route(data))