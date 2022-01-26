# -*- coding: utf-8 -*-
{
    'name': "Busines",
    'sequence': 10,
    'summary': """
        Business Profiles of the service providers
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Billionthings.io",
    'website': "http://billiothings.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/business_profile.xml',
        'views/web_profile.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'license': 'LGPL-3',
}
