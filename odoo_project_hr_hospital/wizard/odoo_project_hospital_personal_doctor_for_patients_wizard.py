from odoo import models, fields


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
