from odoo import models, fields


class HRHospitalDoctors(models.Model):
    _name = 'odoo.project.hospital.doctors'
    _description = 'Doctors'
    _inherit = "odoo.project.hospital.person"
    _rec_name = 'full_name'

    specialization_id = fields.Many2one(
        comodel_name='odoo.project.hospital.specialization',
        string='Specialization',
        help='Specialization',
    )
    intern = fields.Boolean(
        default=False,
    )
    mentor_doctor_id = fields.Many2one(
        comodel_name='odoo.project.hospital.doctors',
        string='Mentor doctor',
        help='Mentor doctor',
    )
    intern_ids = fields.One2many(
        comodel_name='odoo.project.hospital.doctors',
        inverse_name='mentor_doctor_id',
        string='Interns',
        help='Interns',
    )

    def open_patient_visit_act_window_calendar(self):
        action = {
            'name': 'Patient Visit',
            'type': 'ir.actions.act_window',
            'res_model': 'odoo.project.hospital.visits',
            'domain': [('doctor_id', '=', self.id)],
            'context': {
                'personal_doctor_id': self.id,
            },
            'view_mode': 'calendar',
            'view_id': self.env.ref('odoo_project_hr_hospital.odoo_project_hospital_visits_calendar').id,
        }
        return action
