{
    'name': "Website Search Product Tags",
    'summary': """Search website products by tags""",
    'category': 'eCommerce',
    'version': '11.0.1.0.3',
    'application': False,
    'author': 'Mediterranean Apps',
             
    'license': 'GPL-3',
    "support": "mediterranean.apps@gmail.com",
    'price': 14.0,
    'currency': 'EUR',
    'images': ['images/search.png'],
    'depends': ['website_sale', 'product_tags'],
    'post_load': None,
    'pre_init_hook': None,
    'post_init_hook': None,

    'auto_install': False,
    'installable': True,
    'data': [
        'views/tours.xml',
    ],
}
