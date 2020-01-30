{
    "name": """Multi Website support in eCommerce""",
    "summary": """Multi Website support in eCommerce""",
    "category": "eCommerce",
    "images": ["images/website_multi_company_sale_main.png"],
    "version": "12.0.1.5.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": [
        "ma_website_multi_company",
        "website_sale",
        "ir_rule_website",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/product_public_category_views.xml",
        "views/res_config_views.xml",
        "views/product_template_views.xml",
        "views/payment_views.xml",
        "views/sale_views.xml",
        "security/website_multi_company_sale_security.xml",
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
