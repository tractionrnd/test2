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

    def _get_click_values_from_route(self, route_values):
        data = super(ExtLinkTrackerClick, self)._get_click_values_from_route(route_values)

        uname = 'no'
        uemail = 'nono'
        if self.env.user:
            uname = self.env.user.name
            uemail = self.env.user.email

        data.update({
            'x_user_name': uname, #route_values['uname'],
            'x_user_email': uemail #route_values['uemail']
        })

        return data
