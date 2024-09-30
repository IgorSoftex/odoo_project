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
        'views/odoo_project_hospital_menu.xml',
        'views/odoo_project_hospital_doctors_views.xml',
        'views/odoo_project_hospital_patients_views.xml',
        'views/odoo_project_hospital_diseases_views.xml',
        'views/odoo_project_hospital_visits_views.xml',
        'views/odoo_project_hospital_diagnosis_views.xml',
        'views/odoo_project_hospital_contact_person_views.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],
}
