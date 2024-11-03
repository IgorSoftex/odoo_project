from odoo import models, fields


class HRHospitalVisits(models.Model):
    _name = 'odoo.project.hospital.visits'
    _description = 'Patient Visits'

    description = fields.Text(
        string='Symptoms',
        help='Description of symptoms',
    )
    active = fields.Boolean(
        default=True,
    )
