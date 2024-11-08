from odoo.tests import TransactionCase

"""
TransactionCase
   setUpClass()         - метод, котрий викликається перед виконанням тестових методів
       setUp()          - дозволяє виконувати певні дії перед виконанням тестового методу.
       test_method_1() 
       tearDown()       - дозволяє виконувати певні дії після виконанням тестового методу.

       setUp()
       test_method_1()
       tearDown()
   tearDownClass()      - метод, котрий викликається після виконання всіх тестових методів
"""


class TestForLearningCommon(TransactionCase):
    """
    This test created for learning only
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print('class TestForLearningCommon(TransactionCase) from common.py')
