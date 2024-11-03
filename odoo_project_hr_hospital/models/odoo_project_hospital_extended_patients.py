from datetime import date
from odoo import models, fields, api


class HRHospitalExtendedPatients(models.Model):
    _inherit = "odoo.project.hospital.patients"

    personal_doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Personal Doctor',
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
    visits_ids = fields.One2many(
        comodel_name='odoo.project.hospital.visits',
        inverse_name='patient_id',
        string='Visits',
        help='Patient Visits',
    )
    diagnosis_ids = fields.One2many(
        comodel_name='odoo.project.hospital.diagnosis',
        compute='_get_diagnosis',
        string='Diagnosis',
        help='Diagnosis',
    )
    last_visit_state = fields.Char(
        string='Last Visit State',
        compute='compute_last_visit_state',
        # store=True,
    )

    @api.depends('date_of_birth')
    def _compute_age(self):
        for patient in self:
            if patient.date_of_birth:
                patient.age = date.today().year - patient.date_of_birth.year
            else:
                patient.age = 0

    def _get_diagnosis(self):
        for record in self:
            record.diagnosis_ids = [(6, 0, record.env['odoo.project.hospital.visits'].search(
                [('patient_id', '=', record.id)]).diagnosis_ids.ids)]

    def compute_last_visit_state(self):
        for record in self:
            record.last_visit_state = record.env['odoo.project.hospital.visits'].search(
                [('patient_id', '=', record.id)],
                limit=1,
                order='visit_date desc',
            ).state
