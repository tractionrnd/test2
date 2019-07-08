from odoo import api, fields, models

class ExtResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    x_tricolops_webserverl = fields.Char(string=u'Tricolops')

    @api.model
    def get_values(self):
        res = super(ExtResConfigSettings, self).get_values()
        res.update(
            x_tricolops_webserverl = self.env['ir.config_parameter'].sudo().get_param('tcrm_tricolops.x_tricolops_webserverl') or 'http://localhost:8080/data'
        )
        return res

    @api.multi
    def set_values(self):
        super(ExtResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('tcrm_tricolops.x_tricolops_webserverl', self.x_tricolops_webserverl)