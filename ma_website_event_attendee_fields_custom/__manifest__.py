{
    "name": """Event guest info""",
    "summary": """Ask information on registration and stores at Partner record""",
    "category": "Marketing",
    "images": ["images/banner.jpg"],
    "version": "10.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",

    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": [
        "ma_website_event_attendee_fields",
        "partner_contact_birthdate",
        "partner_firstname",
        "partner_identification",
        "partner_contact_nationality",
        "website_event_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/event_event_attendee_field_data.xml",
        "views/website_event_templates.xml",
    ],
    "qweb": [
    ],
    "demo": [
        "data/event_event_demo.yml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
