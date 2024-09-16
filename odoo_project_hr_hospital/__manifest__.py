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
        'views/odoo_project_hr_hospital_menu.xml',
        'views/odoo_project_hr_hospital_doctors_views.xml',
        'views/odoo_project_hr_hospital_patients_views.xml',
        'views/odoo_project_hr_hospital_diseases_views.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],
}
