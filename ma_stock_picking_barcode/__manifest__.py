 
 
 
 
 
{
    "name": "Barcode scanner support for Stock Picking",
    "summary": """The module allows you to process Pickings by barcode scanner via special page /barcode/web (the same as it was in odoo 8.0)""",
    "category": "Warehouse",
    "images": ['images/stock_picking_barcode_main.png'],
    "version": "11.0.1.1.1",

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",

    "license": "LGPL-3",
    'price': 30.00,
    'currency': 'EUR',

    "depends": [
        "stock",
        "web_editor",
        "website",
    ],
    "external_dependencies": {"python": [], "bin": []},

    "data": [
        'views/package_report.xml',
        'views/stock.xml',
        'views/stock_view.xml',
        'views/stock_dashboard.xml',
    ],
    "qweb": [
        'static/src/xml/picking.xml',
    ],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
}
