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
    visit_date = fields.Datetime(
        string='Actual visit date',
        # required=True,
        help='Actual date of visit',
    )
    scheduled_visit_date = fields.Datetime(
        string='Scheduled visit date',
        # required=True,
        help='Scheduled date of visit',
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
            if visit.scheduled_visit_date:
                visit.name = (str(visit.scheduled_visit_date)
                              + ' ' + visit.patient_id.name
                              + ' ' + visit.patient_id.surname
                              + '; doctor: ' + visit.doctor_id.name
                              + ' ' + visit.doctor_id.surname
                              )
            elif visit.visit_date:
                visit.name = (str(visit.visit_date)
                              + ' ' + visit.patient_id.name
                              + ' ' + visit.patient_id.surname
                              + '; doctor: ' + visit.doctor_id.name
                              + ' ' + visit.doctor_id.surname
                              )
            else:
                visit.name = ''

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
