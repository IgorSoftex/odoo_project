import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)

class HRHospitalDoctors(models.Model):
    _name = 'odoo.project.hospital.doctors'
    _description = 'Doctors'

    name = fields.Char()
    active = fields.Boolean(default=True)
    description = fields.Text()
