from datetime import datetime, time
from odoo import models, fields, api
from odoo.exceptions import UserError


class HRHospitalExtendedVisits(models.Model):
    _inherit = "odoo.project.hospital.visits"
    _order = "visit_date DESC"

    name = fields.Char(
        string="Who's visit",
        compute='_compute_visit_name',
        store=False,
        readonly=True,
    )
    state = fields.Selection(
        string="Visit state",
        default='planned',
        selection=[('planned', 'Planned'),
                   ('completed', 'Completed'),
                   ('cancelled', 'Cancelled'),
                   ]
    )
    scheduled_visit_date = fields.Datetime(
        string='Scheduled visit date',
        # required=True,
        help='Scheduled date of visit',
    )
    visit_date = fields.Datetime(
        string='Actual visit date',
        # required=True,
        help='Actual date of visit',
    )
    diagnosis_ids = fields.One2many(
        comodel_name='odoo.project.hospital.diagnosis',
        inverse_name='visit_id',
        string='Diagnosis',
        help='Diagnosis',
    )
    patient_id = fields.Many2one(
        comodel_name='odoo.project.hospital.patients',
        string='Patient',
        help='Patient',
    )
    doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Doctor',
        help='Doctor',
    )

    @api.depends('visit_date', 'patient_id', 'doctor_id')
    def _compute_visit_name(self):
        for visit in self:
            scheduled_visit_date_str = self._get_date_str(visit.scheduled_visit_date)
            visit_date_str = self._get_date_str(visit.visit_date)
            patient_name = self._get_patient_full_name(visit.patient_id)
            doctor_name = self._get_doctor_full_name(visit.doctor_id)
            if visit_date_str:
                visit.name = visit_date_str + ' ' + patient_name + ' ' + doctor_name
            else:
                visit.name = scheduled_visit_date_str + ' ' + patient_name + ' ' + doctor_name

    def _get_date_str(self, visit_date):
        if visit_date:
            date_str = str(visit_date)
        else:
            date_str = ''

        return date_str

    def _get_patient_full_name(self, patient_id):
        if patient_id:
            patient_name = patient_id.name + ' ' + patient_id.surname
        else:
            patient_name = ''
        patient_name = 'patient: ' + patient_name + ';'

        return patient_name

    def _get_doctor_full_name(self, doctor_id):
        if doctor_id:
            doctor_name = doctor_id.name + ' ' + doctor_id.surname
        else:
            doctor_name = ''
        doctor_name = 'doctor: ' + doctor_name + ';'

        return doctor_name

    @api.ondelete(at_uninstall=False)
    def _unlink_visit(self):
        if self.diagnosis_ids:
            raise UserError('The visit has diagnosis!')

    @api.constrains('scheduled_visit_date', 'patient_id', 'doctor_id')
    def _check_unique_visit(self):
        records = self.search(
            [('scheduled_visit_date', '>=', datetime.combine(self.scheduled_visit_date, time.min)),
             ('scheduled_visit_date', '<=', datetime.combine(self.scheduled_visit_date, time.max)),
             ('patient_id', '=', self.patient_id.id),
             ('doctor_id', '=', self.doctor_id.id),
             ])
        if records and len(records) > 1:
            raise UserError("It can't be two visits of the patient to the doctor on this day")
