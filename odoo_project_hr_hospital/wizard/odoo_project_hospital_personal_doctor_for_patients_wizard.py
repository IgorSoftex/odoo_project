from odoo import models, fields, api


class HRHospitalPersonalDoctorForPatients(models.TransientModel):
    _name = 'odoo.project.hospital.personal.doctor.for.patients.wizard'
    _description = 'Appoints a personal doctor for patients'

    patient_ids = fields.Many2many(
        comodel_name='odoo.project.hospital.patients',
        relation="odoo_project_hospital_personal_doctor_for_patients_rel",
        string='Patient',
        help='Patient',
    )
    doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Doctor',
        help='Doctor',
    )

    def appoint_a_personal_doctor(self):
        self.patient_ids.update({
            'personal_doctor_id': self.doctor_id.id,
        })

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self.env.context.get('active_ids'):
            patient_ids = self.env['odoo.project.hospital.patients'].browse(self.env.context.get('active_ids'))
            res['patient_ids'] = patient_ids
        return res
