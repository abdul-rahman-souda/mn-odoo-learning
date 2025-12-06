from odoo import models, fields, api
import logging

from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(required=1)
    phone = fields.Char()
    address = fields.Char()

    proerty_ids = fields.One2many('property','owner_id')