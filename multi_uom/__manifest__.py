{
    'name': 'Multi UOM',
    'category': 'Sale',
    'author': 'Asia Matrix',
    'version': '1.0',
    'depends': [
        'sale',
        'point_of_sale',
        'purchase',
        'stock',
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/decimal_precision.xml',
        'views/assets.xml',
        'views/pos_views.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/stock_views.xml',
        'views/account_move_views.xml',
        'wizards/stock_picking_return.xml',
    ],
    'qweb': [
        'static/src/xml/Buttons/ChangeUOMButton.xml',
        'static/src/xml/Popups/MultiUOMPopup.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'multi_uom/static/src/xml/Buttons/ChangeUOMButton.xml',
            'multi_uom/static/src/xml/Popups/MultiUOMPopup.xml',
            'multi_uom/static/src/xml/Screens/ProductScreen/OrderLine.xml',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
