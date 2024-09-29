from odoo import models, fields, api


class Person(models.AbstractModel):
    """
    This is an abstract model
    """
    _name = "odoo.project.hospital.person"
    _description = "Person (abstract)"

    name = fields.Char(
        translate=True,
        size=100,
    )
    surname = fields.Char(
        translate=True,
        size=100,
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
        max_width=512,
        max_height=512,
    )
