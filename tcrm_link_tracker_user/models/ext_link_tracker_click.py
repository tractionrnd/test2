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
    def add_click(self, code, ip, country_code, uid, stat_id=False):
        self = self.sudo()
        code_rec = self.env['link.tracker.code'].search([('code', '=', code)])

        if not code_rec:
            return None

        again = self.search_count([('link_id', '=', code_rec.link_id.id), ('ip', '=', ip)])

        if not again:
            self.create(
                self._get_click_values_from_route(dict(
                    code=code,
                    ip=ip,
                    country_code=country_code,
                    stat_id=stat_id,
                    uid=uid
                )))

    def _get_click_values_from_route(self, route_values):
        data = super(ExtLinkTrackerClick, self)._get_click_values_from_route(route_values)

        uname = 'no'
        uemail = 'nono'
        if self.env.user:
            uname = self.env.user.name
            uemail = self.env.user.email

        data.update({
            'x_user_name': route_values['uid'],
            'x_user_email': route_values['uid']
        })

        return data
