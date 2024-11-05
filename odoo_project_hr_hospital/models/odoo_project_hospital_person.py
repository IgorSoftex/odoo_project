from odoo import models, fields, api


class Person(models.AbstractModel):
    """
    This is an abstract model
    """
    _name = "odoo.project.hospital.person"
    _description = "Person (Abstract)"
    _order = "surname ASC, name ASC"
    _rec_names_search = ['name', 'surname']

    description = fields.Text()
    name = fields.Char(
        translate=True,
        size=100,
    )
    surname = fields.Char(
        translate=True,
        size=100,
    )
    full_name = fields.Char(
        string="Full name",
        compute='_compute_full_name',
        store=False,
        readonly=True,
    )
    phone = fields.Char(
        size=40,
    )
    gender = fields.Selection(
        default='other',
        selection=[('male', 'Male'),
                   ('female', 'FeMale'),
                   ('other', 'Other/Undefined'), ]
    )
    photo = fields.Image(
        max_width=128,
        max_height=128,
    )
    active = fields.Boolean(
        default=True,
    )

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
    )

    @api.depends('name', 'surname')
    def _compute_full_name(self):
        for person in self:
            if person.name and person.surname:
                person.full_name = person.name + ' ' + person.surname
            else:
                person.full_name = ''
