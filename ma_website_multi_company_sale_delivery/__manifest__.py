 
 
{
    "name": """Real Multi Website (eCommerce Delivery extension)""",
    "summary": """Configure Delivery Carriers list per website""",
    "category": "eCommerce",
    "images": ["images/website_multi_company_sale_delivery_main.png"],
    "version": "11.0.1.0.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 7.00,
    "currency": "EUR",

    "depends": [
        "website_sale_delivery",
        "ir_rule_website",
        "ma_website_multi_company",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/website_multi_company_sale_delivery_security.xml",
        "security/ir.model.access.csv",
        "views/delivery_views.xml",
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
