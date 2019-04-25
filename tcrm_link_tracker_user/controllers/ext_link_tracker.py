from odoo.addons.link_tracker.controller.main import LinkTracker
import werkzeug

from odoo import http
from odoo.http import request

class ExtLinkTracker(LinkTracker):
    @http.route('/r/<string:code>', type='http', auth='none', website=True)
    def full_url_redirect(self, code, **post):
        country_code = request.session.geoip and request.session.geoip.get('country_code') or False
        request.env['link.tracker.click'].add_click(code, request.httprequest.remote_addr, country_code, request.uid, stat_id=False)
        redirect_url = request.env['link.tracker'].get_url_from_code(code)
        return werkzeug.utils.redirect(redirect_url or '', 301)
