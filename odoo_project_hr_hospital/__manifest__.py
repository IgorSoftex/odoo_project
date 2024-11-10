{
    'name': 'HR Hospital (Odoo school)',
    'description': "Module for Odoo school course",
    'summary': "Odoo module for hospital",
    'version': '17.0.1.0.0',
    'category': 'Customizations',
    'license': 'LGPL-3',
    'website': 'https://odoo.school/',
    'author': 'Ihor Pastushenko, the novice programmer',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/odoo_project_hr_hospital_groups.xml',
        'security/odoo_project_hr_hospital_rules.xml',
        'security/ir.model.access.csv',
        'wizard/odoo_project_hospital_personal_doctor_for_patients_wizard_views.xml',
        'wizard/odoo_project_hospital_diseases_report_wizard_view.xml',
        'wizard/odoo_project_hospital_appoint_patient_for_visits_wizard_views.xml',
        'views/odoo_project_hospital_menu.xml',
        'views/odoo_project_hospital_doctors_views.xml',
        'views/odoo_project_hospital_patients_views.xml',
        'views/odoo_project_hospital_diseases_views.xml',
        'views/odoo_project_hospital_diseases_category_views.xml',
        'views/odoo_project_hospital_visits_views.xml',
        'views/odoo_project_hospital_diagnosis_views.xml',
        'views/odoo_project_hospital_contact_person_views.xml',
        'views/odoo_project_hospital_specialization_views.xml',
        'report/odoo_project_hospital_doctors_report.xml',
    ],

    'demo': [
        'demo/specialization_demo_data.xml',
        'demo/diseases_category_demo_data.xml',
        'demo/diseases_demo_data.xml',
        'demo/doctor_demo_data.xml',
        'demo/patient_demo_data.xml',
        'demo/visits_demo_data.xml',
        'demo/diagnosis_demo_data.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
        'static/description/main.jpeg',
    ],
}
