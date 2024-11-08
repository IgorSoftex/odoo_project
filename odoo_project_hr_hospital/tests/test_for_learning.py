from odoo.addons.odoo_project_hr_hospital.tests.common import TestForLearningCommon
from odoo.tests import tagged, users


@tagged('post_install', '-at_install')
class TestForLearning(TestForLearningCommon):
    """
    This test created for learning only
    """

    @classmethod
    def setUpClass(cls):
        super(TestForLearning, cls).setUpClass()
        print('class TestForLearning(TransactionCase) from test_for_learning.py')

    def test_01_print_only(self):
        """
        This test print message only
        """
        print('test_01_print_only - first test')
        return True

