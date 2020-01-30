{
    "name": """Real Multi Website (portal extension)""",
    "summary": """Multi Website support in Portal""",
    "category": "Portal",
    "images": ["images/website_multi_company_portal_main.png"],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": [
        "ma_website_multi_company",
        "portal",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
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
