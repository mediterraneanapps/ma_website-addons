 
 
 
{
    "name": """Upload Multiple Images at Once""",
    "summary": """Great tool to upload multiple images at once""",
    "category": "Extra Tools",
    "images": ["images/multi_images_main.jpg"],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
  
    "license": "LGPL-3",
    "price": 10.00,
    "currency": "EUR",

    "depends": [
        "website_sale",
        "web_multi_attachment_base",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/view.xml",
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

    "demo_title": "Upload Multiple Images at Once",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "multi-product-images",
    "demo_summary": "Upload Multiple Images at Once",
    "demo_images": [
        "images/multi_images_main.jpg",
    ]
}
