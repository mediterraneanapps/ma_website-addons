{
    "name": """Website Demo Data""",
    "summary": """Provides demo websites""",
    "category": "Hidden",
    "images": [],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": [
        "ma_website_multi_company_sale",
        "ma_website_multi_company_blog",
        "theme_bootswatch",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
    ],
    "qweb": [
    ],
    "demo": [
        "demo/res.company.csv",
        "demo/website.csv",
        "demo/product_public_category_demo.xml",
        "demo/product.template.csv",
        "demo/ir.ui.view.csv",
        "demo/website_page.xml",
        "demo/website.menu.csv",
        "demo/website_templates.xml",
        "demo/website_homepage.xml",
        "demo/website_blog.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
