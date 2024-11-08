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
        # print('cls.access_group_manager:', cls.access_group_manager.name, cls.access_group_manager.id)

        """Let's create users"""
        cls.administrator_user = cls.env['res.users'].create({
            'name': 'AdministratorForTest',
            'login': 'administrator_for_test',
            'password': 'administrator_for_test',
            'email': 'administrator_for_test@ukr.net',
            'groups_id': [(6, 0, cls.access_group_administrator.ids)],
        })
        # print('cls.administrator_user:', cls.administrator_user.name, cls.administrator_user.id,
        #       cls.administrator_user.groups_id)
        # for user_group in cls.administrator_user.groups_id:
        #     print('       user_group', user_group.name, user_group.id)
        """
        cls.administrator_user: AdministratorForTest    13  res.groups(12, 1, 7)
            user_group  Administrator       12
            user_group  Internal User       1
            user_group  Technical Features  7
        """

        cls.manager_user = cls.env['res.users'].create({
            'name': 'ManagerForTest',
            'login': 'manager_for_test',
            'password': 'manager_for_test',
            'email': 'manager_for_test@ukr.net',
            'groups_id': [(6, 0, cls.access_group_manager.ids)],
        })
        # print('cls.manager_user:', cls.manager_user.name, cls.manager_user.id, cls.manager_user.groups_id)
        # for user_group in cls.manager_user.groups_id:
        #     print('       user_group', user_group.name, user_group.id)
        """
        cls.manager_user: ManagerForTest 14 res.groups(13, 1, 7)
            user_group  Manager             13
            user_group  Internal User       1
            user_group  Technical Features  7        
        """

        cls.patient_user = cls.env['res.users'].create({
            'name': 'PatientForTest',
            'login': 'patient_for_test',
            'password': 'patient_for_test',
            'email': 'patient_for_test@ukr.net',
            'groups_id': [(6, 0, cls.access_group_patient.ids)],
        })
        # print('cls.patient_user:', cls.patient_user.name, cls.patient_user.id, cls.patient_user.groups_id)
        # for user_group in cls.patient_user.groups_id:
        #     print('       user_group', user_group.name, user_group.id)
        """
        cls.patient_user: PatientForTest 15 res.groups(14, 1, 7)
            user_group  Patient             14
            user_group  Internal User       1
            user_group  Technical Features  7        
        """

        cls.doctor_user = cls.env['res.users'].create({
            'name': 'DoctorForTest',
            'login': 'doctor_for_test',
            'password': 'doctor_for_test',
            'email': 'doctor_for_test@ukr.net',
            'groups_id': [(6, 0, cls.access_group_doctor.ids)],
        })
        # print('cls.doctor_user:', cls.doctor_user.name, cls.doctor_user.id, cls.doctor_user.groups_id)
        # for user_group in cls.doctor_user.groups_id:
        #     print('       user_group', user_group.name, user_group.id)
        """
        cls.doctor_user: DoctorForTest 16 res.groups(16, 1, 7)
            user_group  Doctor                 16
            user_group  Internal User       1
            user_group  Technical Features  7        
        """

        cls.intern_user = cls.env['res.users'].create({
            'name': 'InternForTest',
            'login': 'intern_for_test',
            'password': 'intern_for_test',
            'email': 'intern_for_test@ukr.net',
            'groups_id': [(6, 0, cls.access_group_intern.ids)],
        })
        # print('cls.intern_user:', cls.intern_user.name, cls.intern_user.id, cls.intern_user.groups_id)
        # for user_group in cls.intern_user.groups_id:
        #     print('       user_group', user_group.name, user_group.id)
        """
        cls.intern_user: InternForTest 17 res.groups(15, 1, 7)
            user_group  Intern              15
            user_group  Internal User       1
            user_group  Technical Features  7        
        """

        """Let's create a doctor"""
        cls.doctor = cls.env['odoo.project.hospital.doctors'].create({
            'partner_id': cls.doctor_user.partner_id.id,
            'name': 'DoctorForTest',
        })
        # print('cls.doctor:', cls.doctor.name, cls.doctor.id)
        """
        cls.doctor: DoctorForTest 7
        """

        """Let's create an intern"""
        cls.intern = cls.env['odoo.project.hospital.doctors'].create({
            'partner_id': cls.intern_user.partner_id.id,
            'name': 'InternForTest',
            'intern': True,
        })
        # print('cls.intern:', cls.intern.name, cls.intern.id, cls.intern.intern)
        """
        cls.intern: InternForTest 10 True
        """

        """Let's create a patient"""
        cls.patient = cls.env['odoo.project.hospital.patients'].create({
            'partner_id': cls.patient_user.partner_id.id,
            'name': 'PatientForTest',
        })
        # print('cls.patient:', cls.patient.name, cls.patient.id)
        """
        cls.patient: PatientForTest 5
        """
