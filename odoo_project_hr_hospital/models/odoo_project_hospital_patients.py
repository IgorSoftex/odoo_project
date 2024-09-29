import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalPatients(models.Model):
    _name = 'odoo.project.hospital.patients'
    _description = 'Patients'
    _inherit = "odoo.project.hospital.person"

    active = fields.Boolean(default=True)
    description = fields.Text()
