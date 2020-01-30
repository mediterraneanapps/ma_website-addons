{
    'name': "Product price factor for web shop",
    'summary': """Multiplies price depending on product attributes""",
    'category': 'Website',
    'license': 'GPL-3',
    'author': "Mediterranean Apps",
    'price': 7.00,
    'currency': 'EUR',
    'images': ['images/1.png'],
    "support": "mediterranean.apps@gmail.com",

    'version': '11.0.1.0.0',
    'depends': ['website_sale', 'ma_product_price_factor'],
    'data': [
        'views/templates.xml',
    ],
    'auto_install': True,
    'installable': True,
}
