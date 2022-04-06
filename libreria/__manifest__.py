# -*- coding: utf-8 -*-
{
    'name': "Libreria",

    'summary': """Módulo para la gestión de una librería""",

    'description': """
        Descripción larga
    """,

    'author': "César Redondo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
        'reports/report_libro.xml',
        'reports/report_libro2.xml',
        'data/data.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}