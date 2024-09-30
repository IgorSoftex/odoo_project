import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HRHospitalPatients(models.Model):
    _name = 'odoo.project.hospital.patients'
    _description = 'Patients'
    _inherit = "odoo.project.hospital.person"
    _rec_name = 'full_name'
