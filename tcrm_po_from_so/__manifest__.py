# -*- coding: utf-8 -*-
{
    'name': "Traction - Create PO from SO",

    'summary': "",

    'description': "",

    'author': "TractionCRM",
    'website': "https://www.tractioncrm.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.20',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'purchase'],

    # always loaded
    'data': [
        'views/ext_sale_order.xml'
    ]#,
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #]
}