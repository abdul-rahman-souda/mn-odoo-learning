from odoo import models, fields, api
import logging

from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    property_id = fields.Many2one('property')

    def action_confirm(self):
        res = super(SaleOrder,self).action_confirm()
        _logger.info("error: inside action_confirm method")
        return res
