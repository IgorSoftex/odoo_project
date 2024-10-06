from datetime import datetime
from odoo import models, fields, api


class HRHospitalDiseasesReport(models.TransientModel):
    _name = 'odoo.project.hospital.diseases.report.wizard'
    _description = 'Diseases Report'

    begin_date = fields.Date(
        string='Start of period',
    )
    end_date = fields.Date(
        string='Period end',
    )
    doctor_ids = fields.Many2many(
        comodel_name='odoo.project.hospital.doctors',
        relation="odoo_project_hospital_doctors_report_wizard_rel",
        string='Doctor',
        help='Doctor',
    )
    diseases_ids = fields.Many2many(
        comodel_name='odoo.project.hospital.diseases',
        relation="odoo_project_hospital_diseases_report_wizard_rel",
        string='Diseases',
        help='Diseases',
    )

    def run_diseases_report(self):
        domain = [
            ('visit_id.visit_date', '>=', self.begin_date),
            ('visit_id.visit_date', '<=', self.end_date),
        ]
        if self.doctor_ids:
            domain.append(('visit_id.doctor_id', 'in', self.doctor_ids.ids))
        if self.diseases_ids:
            domain.append(('disease_id', 'in', self.diseases_ids.ids))
        diagnoses = self.env['odoo.project.hospital.diagnosis'].search(domain)
        return {
            'name': 'Disease Report',
            'type': 'ir.actions.act_window',
            'res_model': 'odoo.project.hospital.diagnosis',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', diagnoses.ids)],
            'context': {'group_by': 'disease_id'},
        }

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['begin_date'] = datetime.today().replace(day=1)
        res['end_date'] = datetime.now()
        if self.env.context.get('active_ids'):
            doctor_ids = (self.env['odoo.project.hospital.doctors'].
                          browse(self.env.context.get('active_ids')))
            res['doctor_ids'] = doctor_ids
        return res
