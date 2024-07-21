# -*- coding: utf-8 -*-
{
    'name': "branch_task",
    'summary': """Branch Task""",
    'description': """Branch Task""",
    'author': "Fager Mohsen",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'mail', 'account', 'product', 'sale', 'stock', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'data/branches_seq.xml',
        'data/stock_request_seq.xml',
        'wizard/stock_quant_inherit_view.xml',
        'views/menu.xml',
        'views/branches_view.xml',
        'views/stock_request_view.xml',
        'views/controller_view.xml',
    ],
}
