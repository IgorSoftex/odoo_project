from odoo import models, fields, api


class HRHospitalAppointPatientForVisits(models.TransientModel):
    _name = 'odoo.project.hospital.appoint.patient.for.visits.wizard'
    _description = 'Appoints a patient for visits'

    visit_ids = fields.Many2many(
        comodel_name='odoo.project.hospital.visits',
        relation="odoo_project_hospital_appoint_patient_for_visits_rel",
        string='Visits',
        help='Visits',
    )
    patient_id = fields.Many2one(
        comodel_name='odoo.project.hospital.patients',
        string='Patient',
        help='Patient',
    )

    def appoint_patient_for_visits(self):
        # self.visit_ids.update({
        #     'patient_id': self.patient_id.id,
        # })
        if self.patient_id:
            for visit in self.visit_ids:
                visit.patient_id = self.patient_id

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self.env.context.get('active_ids'):
            visit_ids = (self.env['odoo.project.hospital.visits']
                         .browse(self.env.context.get('active_ids')))
            res['visit_ids'] = visit_ids
        return res
