from odoo import models, fields, api


class HRHospitalDiseasesCategory(models.Model):
    """
    This is a module for diseases categories
    """
    _name = 'odoo.project.hospital.diseases.category'
    _description = 'Diseases category'
    _parent_name = "parent_id"
    _parent_store = True
    # _rec_name = 'complete_name'
    _order = 'name'

    name = fields.Char(
        translate=True,
    )
    complete_name = fields.Char(
        string='Complete Name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
        translate=True,
    )
    parent_id = fields.Many2one(
        comodel_name='odoo.project.hospital.diseases.category',
        string='Parent Category',
        index=True,
        ondelete='cascade',
    )
    parent_path = fields.Char(
        index=True,
        unaccent=False
    )
    child_id = fields.One2many(
        comodel_name='odoo.project.hospital.diseases.category',
        inverse_name='parent_id',
        string='Child Category',
    )
    active = fields.Boolean(
        default=True
    )
    description = fields.Text(
        translate=True,
    )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        """
        This method computes a complete name
        """
        for disease_category in self:
            if disease_category.parent_id:
                disease_category.complete_name = '%s / %s' % (
                    disease_category.parent_id.complete_name,
                    disease_category.name
                )
            else:
                disease_category.complete_name = disease_category.name
