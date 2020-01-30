{
    "name": """Product swap at eCommerce""",
    "summary": """Product upgrading / changing feature for your online shop""",
    "category": "eCommerce",
    "images": ["images/banner.jpg"],
    "version": "10.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 14.00,
    "currency": "EUR",

    "depends": [
        "website_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/product.xml",
        "views/website_sale_templates.xml",
        "views/sale_order_views.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
