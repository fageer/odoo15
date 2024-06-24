# -*- coding: utf-8 -*-
{
    'name': "branch_task",
    'summary': """Branch Task""",
    'description': """Branch Task""",
    'author': "Fager Mohsen",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'mail', 'account', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/branches_seq.xml',
        'views/menu.xml',
        'views/branches_view.xml',
    ],
}
