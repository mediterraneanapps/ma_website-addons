 
 
{
    "name": """Real Multi Website (Online Event's Tickets extension)""",
    "summary": """Configure Events' Tickets per website""",
    "category": "Marketing",
    "images": ['images/website_multi_company_event_sale.jpg'],
    "version": "10.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 7.00,
    "currency": "EUR",

    "depends": [
        "ma_website_multi_company",
        "ma_website_event_sale",
        "ir_rule_website",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/event_views.xml",
        "security/event_security.xml",
    ],
    "demo": [
    ],
    "qweb": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
