# -*- coding: utf-8 -*-
{
    'name': "Modul Kedatech",

    'summary': """
        Test Coding Odoo Kedatech version Odoo 14""",

    'description': """
        Test Coding Odoo Kedatech version Odoo 14
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "https://www.linkedin.com/in/ahmaddyd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/material_modul_views.xml',
        'views/supplier_views.xml',
        'report/report.xml',
        'report/material_invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
