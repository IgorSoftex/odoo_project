import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HRHospitalVisits(models.Model):
    _name = 'odoo.project.hospital.visits'
    _description = 'Patient visits'

    name = fields.Char(
        string="Who's visit",
        compute='_compute_visit_name',
        store=False,
        readonly=True,
    )
    visit_date = fields.Datetime(
        string='Visit date',
        required=True)
    active = fields.Boolean(
        default=True)
    description = fields.Text(
        string='Symptoms',
        help='Description of symptoms',
    )
    patient_id = fields.Many2one(
        comodel_name='odoo.project.hospital.patients',
        string='Patient')
    doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Doctor')

    @api.depends('visit_date', 'patient_id', 'doctor_id')
    def _compute_visit_name(self):
        # print('self:', self)
        for visit in self:
            visit.name = (str(visit.visit_date)
                          +' '+visit.patient_id.name+' '+visit.patient_id.surname
                          +'; doctor: '+visit.doctor_id.name+' '+visit.doctor_id.surname
                          )