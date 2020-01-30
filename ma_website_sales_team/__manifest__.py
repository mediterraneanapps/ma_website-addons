{
    'name': 'Sales team in eCommerce',
    'version': '1.0.0',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'eCommerce',
    "support": "mediterranean.apps@gmail.com",
    'description': """
Split products by sales team.

    """,
    'depends': [
        'sales_team',
        'website_sale',
        'ma_website_sale_order',
    ],
    'data': [
        'security/website_sales_team_security.xml',
        'security/ir.model.access.csv',
        'website_sales_team_data.xml',
        'website_sales_team_templates.xml',
        'website_sales_team_views.xml',
    ],
    'installable': True,
}
