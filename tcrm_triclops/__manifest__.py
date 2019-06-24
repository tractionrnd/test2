# -*- coding: utf-8 -*-
{
    'name': "Traction - Triclops Integration",

    'summary': "",

    'description': "",

    'author': "TractionCRM",
    'website': "https://www.tractioncrm.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.8',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'stock', 'delivery'],

    # always loaded
    'data': [
        'views/ext_ext_stock_picking.xml',
        'views/ext_stock_quant_package.xml'
    ]#,
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #]
}