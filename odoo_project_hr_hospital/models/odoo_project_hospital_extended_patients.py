import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HRHospitalExtendedPatients(models.Model):
    _inherit = "odoo.project.hospital.patients"

    personal_doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Personal doctor',
    )
