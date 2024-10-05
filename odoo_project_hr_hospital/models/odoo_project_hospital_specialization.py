from odoo import models, fields


class HRHospitalSpecialization(models.Model):
    _name = 'odoo.project.hospital.specialization'
    _description = 'Specialization'

    name = fields.Char(
        translate=True,
        size=100,
        string='Name',
        help='Specialization name'
    )
    competences = fields.Text(
        string='Competences',
        help='Description of competence',
    )
    active = fields.Boolean(
        default=True
    )
