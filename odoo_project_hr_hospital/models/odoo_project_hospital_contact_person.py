import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class HRHospitalContactPerson(models.Model):
    _name = 'odoo.project.hospital.contact.person'
    _description = 'Contact Person'
    _inherit = "odoo.project.hospital.person"
    _rec_name = 'full_name'
