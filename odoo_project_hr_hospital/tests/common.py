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

        """Let's create access groups"""
        cls.access_group_administrator = cls.env.ref(
            'odoo_project_hr_hospital.group_odoo_project_hr_hospital_administrator')  # Administrator 12
        cls.access_group_manager = cls.env.ref(
            'odoo_project_hr_hospital.group_odoo_project_hr_hospital_manager')  # Manager 13
        cls.access_group_patient = cls.env.ref(
            'odoo_project_hr_hospital.group_odoo_project_hr_hospital_patient')  # Patient 14
        cls.access_group_doctor = cls.env.ref('odoo_project_hr_hospital.group_odoo_project_hr_hospital_doctor')
        cls.access_group_intern = cls.env.ref('odoo_project_hr_hospital.group_odoo_project_hr_hospital_intern')

        """Let's create users"""
        cls.administrator_user = cls.env['res.users'].create({
            'name': 'Administrator user for test',
            'login': 'administrator_user',
            'password': 'administrator_user',
            'email': 'administrator_user@ukr.net',
            'groups_id': [(6, 0, cls.access_group_administrator.ids)],
        })

        cls.manager_user = cls.env['res.users'].create({
            'name': 'Manager user for test',
            'login': 'manager_user',
            'password': 'manager_user',
            'email': 'manager_user@ukr.net',
            'groups_id': [(6, 0, cls.access_group_manager.ids)],
        })

        cls.patient_user = cls.env['res.users'].create({
            'name': 'Patient user for test',
            'login': 'patient_user',
            'password': 'patient_user',
            'email': 'patient_user@ukr.net',
            'groups_id': [(6, 0, cls.access_group_patient.ids)],
        })

        cls.doctor_user = cls.env['res.users'].create({
            'name': 'Doctor user for test',
            'login': 'doctor_user',
            'password': 'doctor_user',
            'email': 'doctor_user@ukr.net',
            'groups_id': [(6, 0, cls.access_group_doctor.ids)],
        })

        cls.intern_user = cls.env['res.users'].create({
            'name': 'Intern user for test',
            'login': 'intern_user',
            'password': 'intern_user',
            'email': 'intern_user@ukr.net',
            'groups_id': [(6, 0, cls.access_group_intern.ids)],
        })

        """Let's create a doctor"""
        cls.doctor = cls.env['odoo.project.hospital.doctors'].create({
            'partner_id': cls.doctor_user.partner_id.id,
            'name': 'Doctor',
            'surname': 'For test',
            'intern': False,
            'phone': '098-001-55-89',
            'gender': 'other',
        })

        """Let's create an intern"""
        cls.intern = cls.env['odoo.project.hospital.doctors'].create({
            'partner_id': cls.intern_user.partner_id.id,
            'name': 'Intern',
            'surname': 'For test',
            'intern': True,
            'phone': '098-001-11-00',
            'gender': 'male',
        })

        """Let's create a patient"""
        cls.patient = cls.env['odoo.project.hospital.patients'].create({
            'partner_id': cls.patient_user.partner_id.id,
            'name': 'Patient',
            'surname': 'For test',
        })
