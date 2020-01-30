{
    "name": """Multi Website Blog""",
    "summary": """Blocks an access to a website blog from websites, which have not been specified as allowed for this blog""",
    "category": "eCommerce",
    "images": ["images/multi_blog_main.png"],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",

    "license": "LGPL-3",
    "price": 7.00,
    "currency": "EUR",

    "depends": [
        "website_blog",
        "ma_website_multi_company",
        "ir_rule_website",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/website_blog_views.xml',
        'security/blog_security.xml',
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
