from odoo import models, fields, api
import logging

from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class Abd(models.Model):
    _name = 'abd'

    name = fields.Char(required=1)
# def abd():

#     return 'hi'