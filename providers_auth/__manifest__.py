# -*- coding: utf-8 -*-
{
    'name': "Provider Auth",

    'summary': 'Billiothings',
    'sequence': 10,
    'description': """
    main goal is to conver the http reidrect to https
    """,

    'author': "My Company",
    'website': 'https://www.odoo.com/app/billing',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','auth_oauth'],

    # always loaded
    'data': [
        
    ],
    # only loaded in demonstration mode
    'demo': [
      
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'assets': {} ,
    'license': 'LGPL-3',
    
}