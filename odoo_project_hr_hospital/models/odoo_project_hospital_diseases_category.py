import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HRHospitalDiseasesCategory(models.Model):
    _name = 'odoo.project.hospital.diseases.category'
    _description = 'Diseases category'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'name'

    name = fields.Char()
    complete_name = fields.Char(
        string='Complete Name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
    )
    parent_id = fields.Many2one(
        comodel_name='odoo.project.hospital.diseases.category',
        string='Parent Category',
        index=True,
        ondelete='cascade',
    )
    parent_path = fields.Char(
        index=True
    )
    child_id = fields.One2many(
        comodel_name='odoo.project.hospital.diseases.category',
        inverse_name='parent_id',
        string='Child Category',
    )
    active = fields.Boolean(
        default=True
    )
    description = fields.Text()

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for disease_category in self:
            if disease_category.parent_id:
                disease_category.complete_name = '%s / %s' % (
                    disease_category.parent_id.complete_name, disease_category.name)
            else:
                disease_category.complete_name = disease_category.name
