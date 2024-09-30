import logging
from datetime import date
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HRHospitalExtendedPatients(models.Model):
    _inherit = "odoo.project.hospital.patients"

    personal_doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Personal doctor',
    )
    date_of_birth = fields.Date(
        string='Date Of Birth',
    )
    age = fields.Integer(
        string="Age",
        compute='_compute_age',
        store=False,
        readonly=True,
    )
    passport_data = fields.Char(
        size=100,
    )
    contact_person_id = fields.Many2one(
        comodel_name='odoo.project.hospital.contact.person',
        string='Contact Person',
    )

    @api.depends('date_of_birth')
    def _compute_age(self):
        for patient in self:
            if patient.date_of_birth:
                patient.age = date.today().year - patient.date_of_birth.year
            else:
                patient.age = 0
