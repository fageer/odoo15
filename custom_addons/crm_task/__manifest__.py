# -*- coding: utf-8 -*-
{
    'name': "CRM Task",
    'summary': """ CRM Task """,
    'description': """ CRM Task """,
    'author': "Fager Mohsen",
    'website': "http://www.github.com/fageer",
    'version': '0.1',
    'depends': ['base', 'crm', 'sale', 'purchase', 'sale_crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/advertiser_view.xml',
        'views/crm_lead_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
}
