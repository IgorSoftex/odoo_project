from odoo import models, fields


class HRHospitalPatients(models.Model):
    _name = 'odoo.project.hospital.patients'
    _description = 'Patients'
    _inherit = "odoo.project.hospital.person"
    _rec_name = 'full_name'

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
    )

    def patient_test_action(self):
        print('partner_id:', self.partner_id.name, self.partner_id.id)
        print('user.partner_id:', self.env.user.partner_id.name, self.env.user.partner_id.id)
