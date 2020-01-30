 
 
 
{
    "name": """Stop Online Sales""",
    "summary": """Adds options to disable all sales and hide all prices, but keep products visible at website""",
    "category": "eCommerce",
    "images": ["images/main.jpg"],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 19.00,
    "currency": "EUR",

    "depends": [
        "website_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "templates.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
