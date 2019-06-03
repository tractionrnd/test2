# -*- coding: utf-8 -*-
{
    'name': "Traction - Mass Mailing Contact Score",

    'summary': "",

    'description': "",

    'author': "TractionCRM",
    'website': "https://www.tractioncrm.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.6',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mass_mailing', 'base_automation', 'marketing_automation'],

    # always loaded
    'data': [
        'views/ir_actions_server.xml'
    ]
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #]
}
