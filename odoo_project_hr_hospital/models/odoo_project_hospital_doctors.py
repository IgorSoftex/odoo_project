import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalDoctors(models.Model):
    _name = 'odoo.project.hospital.doctors'
    _description = 'Doctors'
    _inherit = "odoo.project.hospital.person"
    _rec_name = 'full_name'
