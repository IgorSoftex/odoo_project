import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalDoctors(models.Model):
    _name = 'odoo.project.hospital.doctors'
    _description = 'Doctors'
    _inherit = "odoo.project.hospital.person"
    _rec_name = 'full_name'

    specialization_id = fields.Many2one(
        comodel_name='odoo.project.hospital.specialization',
        string='Specialization',
        help='Specialization',
    )
    intern = fields.Boolean(
        default=False,
    )
    mentor_doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Mentor doctor',
        help='Mentor doctor',
    )
