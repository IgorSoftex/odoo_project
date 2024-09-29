import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HRHospitalDoctors(models.Model):
    _name = 'odoo.project.hospital.doctors'
    _description = 'Doctors'
    _inherit = "odoo.project.hospital.person"

    active = fields.Boolean(default=True)
    description = fields.Text()
