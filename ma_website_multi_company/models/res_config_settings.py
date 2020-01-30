 
 

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_homepage_id = fields.Many2one(related='website_id.homepage_id', string='Homepage', readonly=False)
