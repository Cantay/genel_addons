{
    'name': 'Combo Product',
    'category': 'sale',
    'author': 'Asia Matrix',
    'version': '0.1',
    'depends': ['sale', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/sale_views.xml',
        'views/product_views.xml',
    ],
    'images': ['static/img/main.png'],
    'qweb': ['static/src/xml/OrderLine.xml'],
    'auto_install': False,
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
            'web.assets_qweb': [
                'combo_product/static/src/xml/*',
            ],
        },
}
