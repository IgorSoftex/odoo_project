import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalPatients(models.Model):
    _name = 'odoo.project.hospital.patients'
    _description = 'Patients'

    name = fields.Char()
    active = fields.Boolean(default=True)
    description = fields.Text()
