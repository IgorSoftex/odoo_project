from datetime import datetime
from odoo.addons.odoo_project_hr_hospital.tests.common import TestForLearningCommon
from odoo.tests import tagged, users


@tagged('post_install', '-at_install')
class TestModelMethods(TestForLearningCommon):
    """
    This test created for testing model methods
    """

    @classmethod
    def setUpClass(cls):
        super(TestModelMethods, cls).setUpClass()

    def test_03_model_methods_compute_full_name_for_patient(self):
        """
        Compute full_name for patient
        """
        # print('test_03_model_methods_compute_full_name_for_patient')

        self.assertEqual(self.patient.full_name, "{} {}".format(self.patient.name, self.patient.surname, ))
        return True

    def test_04_model_methods_compute_full_name_for_doctor(self):
        """
        Compute full_name for doctor
        """
        # print('test_04_model_methods_compute_full_name_for_doctor')

        self.assertEqual(self.doctor.full_name, "{} {}".format(self.doctor.name, self.doctor.surname, ))
        return True
