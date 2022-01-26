# -*- coding: utf-8 -*-
{
    'name': "Service Profiles",
    'sequence': 10,
    'summary': """
        Service Profiles of the service providers
        """,

    'description': """
        Service Profiles of the service providers
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
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/service_profile.xml',
        'views/gallery.xml',
        'views/web/create_service_profile.xml',
        'views/web/create_service_address.xml',
        'views/web/create_service_image.xml',
        'views/web/profile_redirect.xml',
        # 'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'service_profiles/static/css/image-uploader.css',
            'service_profiles/static/css/profile.css',
            'service_profiles/static/js/image-uploader.js', 
            'service_profiles/static/js/profile.js',
            'service_profiles/static/js/address-profile.js',
         
        ], },
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'license': 'LGPL-3',
}
