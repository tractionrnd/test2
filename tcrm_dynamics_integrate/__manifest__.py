# -*- coding: utf-8 -*-
{
    'name': "Dynamics - ODOO integration",

    'summary': "",

    'description': "",

    'author': "TractionCRM",
    'website': "https://www.tractioncrm.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.22',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'base_automation', 'crm'],

    # always loaded
    'data': [
	    'views/job_runner.xml',
      'security/ir.model.access.csv'
    ]#,
    #'qweb': [
    #    'views/chatter.xml'
    #],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #]
}