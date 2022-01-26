# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Auth',
    'summary': 'Billiothings',
    'sequence': 10,
    'description': """Billiothings""",
    'author': "Billionthings.io",
    'category': 'Uncategorized',
    'website': 'http://billiothings.io',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_form.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'auth/static/css/auth.css',
            'auth/static/js/auth.js'
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'license': 'LGPL-3',
}
