{
    "name": """Hide "Add To Cart" button from product page""",
    "summary": """Allows to disable product sales via eCommerce for any reason""",
    "category": "eCommerce",
    "images": [],
    "version": "1.0.0",

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": [
        "website_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views.xml",
        "templates.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
}
