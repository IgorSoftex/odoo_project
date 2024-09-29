import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HRHospitalPatients(models.Model):
    _name = 'odoo.project.hospital.patients'
    _description = 'Patients'
    _inherit = "odoo.project.hospital.person"
    _rec_name = 'full_name'

    full_name = fields.Char(
        string="Full name",
        compute='_compute_full_name',
        store=False,
        readonly=True,
    )

    active = fields.Boolean(default=True)
    description = fields.Text()

    @api.depends('name', 'surname')
    def _compute_full_name(self):
        for patient in self:
            patient.full_name = patient.name + ' ' + patient.surname
