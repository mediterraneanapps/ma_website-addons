 
 
 
{
    "name": """E-commerce Category Cache""",
    "summary": """Use this module to greatly accelerate the loading of a page with a large number of product categories""",
    "category": "Website",
    "images": ['images/websale_cache.png'],
    "version": "10.0.1.0.1",

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 19.00,
    "currency": "EUR",

    "depends": [
        "website_sale",
        "website",
        "ma_base_action_rule",
    ],
    "data": [
        "views.xml",
        "data/ir_action_server.xml",
        "data/base_action_rules.xml",
    ],
    "installable": True,
}
