# -*- coding: utf-8 -*-
{
    'name': "Calculator",

    'summary': """
        To calculate with basic arithmetic operators"
    """,

    'description': """
        Starting module for "Discover the JS framework, chapter 1: Owl components"
    """,


    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'application': True,
    'installable': True,
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'odoo_calculator.assets': [

            'odoo_calculator/static/src/**/*',
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            #'web/static/lib/bootstrap/scss/_maps.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),
            'web/static/src/libs/fontawesome/css/font-awesome.css',
        ],
    },
    'license': 'AGPL-3'
}
