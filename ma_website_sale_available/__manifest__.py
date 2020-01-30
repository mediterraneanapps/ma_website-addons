{
    'name': "Sale only available products on Website",
    'summary': """Sale only available products on Website""",
    'version': '11.0.1.0.0',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'eCommerce',
    "support": "mediterranean.apps@gmail.com",
    'images': ['images/available.png'],
    'price': 3.00,
    'currency': 'EUR',
    'depends': [
        'website_sale',
        'stock',
        'delivery',
    ],
    'data': [
        'views/website_sale_available_views.xml',
    ],
    'installable': True,
}
