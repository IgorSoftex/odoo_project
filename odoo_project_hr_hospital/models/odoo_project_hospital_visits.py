import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalVisits(models.Model):
    _name = 'odoo.project.hospital.visits'
    _description = 'Patient visits'

    visit_date = fields.Datetime(
        string='Visit date',
        required=True)
    active = fields.Boolean(
        default=True)
    description = fields.Text()
    patient_id = fields.Many2one(
        comodel_name='odoo.project.hospital.patients',
        string='Patient')
    doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Doctor')
    disease_ids = fields.Many2many(
        comodel_name='odoo.project.hospital.diseases',
        string='Diseases')
