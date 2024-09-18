import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalDiseases(models.Model):
    _name = 'odoo.project.hospital.diseases'
    _description = 'Diseases'

    name = fields.Char()
    active = fields.Boolean(default=True)
    description = fields.Text()
