from datetime import datetime, time
from odoo import models, fields, api
from odoo.exceptions import UserError


class HRHospitalExtendedVisits(models.Model):
    _inherit = "odoo.project.hospital.visits"

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
            visit.name = self._create_visit_name(
                visit.scheduled_visit_date,
                visit.visit_date,
                visit.patient_id,
                visit.doctor_id)

    def _create_visit_name(
            self,
            scheduled_visit_date,
            visit_date,
            patient_id,
            doctor_id):

        if scheduled_visit_date:
            visit_date_str = str(scheduled_visit_date)
        elif visit_date:
            visit_date_str = str(visit_date)
        else:
            visit_date_str = ''

        if patient_id:
            patient_name = patient_id.name + ' ' + patient_id.surname
        else:
            patient_name = ''

        if doctor_id:
            doctor_name = doctor_id.name + ' ' + doctor_id.surname
        else:
            doctor_name = ''

        visit_name = visit_date_str + ' ' + patient_name + ' ' + doctor_name

        return visit_name

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
