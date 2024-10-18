{
    'name': 'hr hospital',
    'description': "Ihor's module",
    'version': '17.0.1.0.0',
    'category': 'Customizations',
    'license': 'OPL-1',
    'website': 'https://odoo.school/',
    'author': 'Ihor',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/ir.model.access.csv',
        'wizard/odoo_project_hospital_personal_doctor_for_patients_wizard_views.xml',
        'wizard/odoo_project_hospital_diseases_report_wizard_view.xml',
        'views/odoo_project_hospital_menu.xml',
        'views/odoo_project_hospital_doctors_views.xml',
        'views/odoo_project_hospital_patients_views.xml',
        'views/odoo_project_hospital_diseases_views.xml',
        'views/odoo_project_hospital_diseases_category_views.xml',
        'views/odoo_project_hospital_visits_views.xml',
        'views/odoo_project_hospital_diagnosis_views.xml',
        'views/odoo_project_hospital_contact_person_views.xml',
        'views/odoo_project_hospital_specialization_views.xml',
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
        'static/description/icon.png'
    ],
}
