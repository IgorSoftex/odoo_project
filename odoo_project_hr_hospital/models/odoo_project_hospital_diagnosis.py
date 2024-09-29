from odoo import models, fields, api


class HRHospitalDiagnosis(models.Model):
    _name = 'odoo.project.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(
        translate=True,
        size=100,
        string='Diagnosis name',
        help='Diagnosis name'
    )
    description = fields.Text(
        string='Treatment',
        help='Prescriptions for treatment',
    )
    visit_id = fields.Many2one(
        comodel_name='odoo.project.hospital.visits',
        string='Patient visit',
        help='Patient visit',
    )
    disease_id = fields.Many2one(
        comodel_name='odoo.project.hospital.diseases',
        string='Disease',
        help='Disease',
    )
    is_approved = fields.Boolean(
        string="Approved",
        help="Diagnosis is approved",
    )
    active = fields.Boolean(
        default=True
    )
