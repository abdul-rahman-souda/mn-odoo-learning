from odoo import models, fields, api
import logging

from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class Client(models.Model):
    _name = 'client'
    _inherit = 'owner'
