
{
    'name': "custom_tasks",
    'summary': """""",
    'description': """ Long description of module's purpose""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'contacts', 'mail', 'account', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_res_partner_view.xml',
        'views/inherit_sale_order_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
