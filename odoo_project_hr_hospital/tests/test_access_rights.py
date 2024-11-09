from datetime import datetime
from odoo.addons.odoo_project_hr_hospital.tests.common import TestForLearningCommon
from odoo.tests import tagged, users
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install')
class TestAccessRights(TestForLearningCommon):
    """
    This test created for testing access rights
    """

    @classmethod
    def setUpClass(cls):
        super(TestAccessRights, cls).setUpClass()

    @users('doctor_user')
    def test_01_access_rights_doctor_can_create_patient(self):
        """
        Access rights: doctor can create a patient
        """
        # print('test_01_access_rights_doctor_can_create_patient')

        visit = self.env['odoo.project.hospital.visits'].create({
            'description': 'Test visit 1',
            'state': 'planned',
            'scheduled_visit_date': datetime.now(),
            'patient_id': self.patient.id,
            'doctor_id': self.doctor.id,
        })
        return True

    @users('patient_user')
    def test_02_access_rights_patient_cannot_create_patient(self):
        """
        Access rights: doctor can't create a patient
        """
        # print('test_02_access_rights_patient_cannot_create_patient')
        with self.assertRaises(AccessError):
            visit = self.env['odoo.project.hospital.visits'].create({
                'description': 'Test visit 2',
                'state': 'planned',
                'scheduled_visit_date': datetime.now(),
                'patient_id': self.patient.id,
                'doctor_id': self.doctor.id,
            })
        return True
