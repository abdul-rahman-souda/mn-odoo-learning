from odoo import models, fields, api
import logging
from . import abd
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class Tag(models.Model):
    _name = 'tag'

    name = fields.Char(required=1)