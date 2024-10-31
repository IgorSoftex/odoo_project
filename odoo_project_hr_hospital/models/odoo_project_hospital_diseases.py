from odoo import models, fields


class HRHospitalDiseases(models.Model):
    _name = 'odoo.project.hospital.diseases'
    _description = 'Diseases'
    _order = 'name'

    name = fields.Char(
        translate=True,
    )
    description = fields.Text(
        translate=True,
    )
    disease_category = fields.Many2one(
        comodel_name='odoo.project.hospital.diseases.category',
        string='Parent Category',
        index=True,
    )
    active = fields.Boolean(
        default=True
    )
