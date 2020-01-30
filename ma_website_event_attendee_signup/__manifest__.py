{
    "name": """Auto Sign Up Event guest""",
    "summary": """Attendees can use portal dashboard to make extra purchases for the event, for example.""",
    "category": "Marketing",
    "images": ["images/banner.jpg"],
    "version": "10.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",

    "license": "AGPL-3",
    "price": 25.00,
    "currency": "EUR",

    "depends": [
        "event",
        "partner_event",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/event_event_views.xml",
        "data/mail_template_data.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
