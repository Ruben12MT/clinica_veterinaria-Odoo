# -*- coding: utf-8 -*-
{
    'name': "Clinica",

    'summary': """
        Clinica Veterinaria 'Los Montes'""",

    'description': """
        Clinica Veterinaria 'Los Montes
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/pet_views.xml',
        'views/appointment_views.xml',
        'views/veterinarian_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/pets_demo.xml',
        'demo/treatments_demo.xml',
        'demo/appointments_demo.xml',

    ],
}
