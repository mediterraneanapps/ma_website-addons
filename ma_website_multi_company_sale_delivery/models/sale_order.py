 
 

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_delivery_methods(self):
        available_carriers = super(SaleOrder, self)._get_delivery_methods()
        delivery_access_user = self.env.ref('ma_website_multi_company_sale_delivery.delivery_carrier_read_user')
        available_carriers = self.env['delivery.carrier'].sudo(delivery_access_user).search([('id', 'in', available_carriers.ids)]).sudo()
        return available_carriers
