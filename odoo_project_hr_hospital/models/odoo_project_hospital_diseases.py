import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalDiseases(models.Model):
    _name = 'odoo.project.hospital.diseases'
    _description = 'Diseases'
    _order = 'name'

    name = fields.Char()
    disease_category = fields.Many2one(
        comodel_name='odoo.project.hospital.diseases.category',
        string='Parent Category',
        index=True,
    )
    active = fields.Boolean(
        default=True
    )
    description = fields.Text()
