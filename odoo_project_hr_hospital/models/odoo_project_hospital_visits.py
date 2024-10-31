from odoo import models, fields


class HRHospitalVisits(models.Model):
    _name = 'odoo.project.hospital.visits'
    _description = 'Patient Visits'

    description = fields.Text(
        string='Symptoms',
        help='Description of symptoms',
        translate=True,
    )
    active = fields.Boolean(
        default=True,
    )
