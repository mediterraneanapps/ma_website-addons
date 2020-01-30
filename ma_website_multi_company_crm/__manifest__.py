 
 
{
    "name": """Real Multi Website (CRM extension)""",
    "summary": """Make CRM features work properly in multi-website environment""",
    "category": "eCommerce",
    "images": ["images/main.jpg"],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",

    "license": "LGPL-3",
    "price": 7.00,
    "currency": "EUR",

    "depends": [
        "crm",
        "ma_website_multi_company",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/crm_lead_views.xml",
        "security/crm_lead_security.xml",
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
