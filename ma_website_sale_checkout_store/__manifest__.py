 
 
 
 
 

{
    'name': """Pickup and pay at store""",
    'summary': """Simplify checkout process by excluding shipping and/or payment information""",
    'category': 'eCommerce',
    'images': ['images/1.png'],
    'version': '12.0.1.0.6',

    'author': 'Mediterranean Apps',
    "support": "mediterranean.apps@gmail.com",
    'license': 'LGPL-3',
    'price': 35.00,
    'currency': 'EUR',

    'depends': [
        'website_sale',
    ],
    'external_dependencies': {'python': [], 'bin': []},
    'data': [
        'templates.xml',
        'views.xml',
        'data/data.xml',
    ],
    "installable": True,
    'auto_install': False,
}
