# -*- coding: utf-8 -*-
{
    'name': "sol_specific",

    'summary': """
        Specific development realized only for sol problematics""",

    'description': """
        Specific development realized only for sol problematics
    """,

    'author': "Aldais",
    'website': "http://www.aldais.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': 'SOL.2023.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',
        'action/purchase_action.xml',
        'action/sale_action.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
