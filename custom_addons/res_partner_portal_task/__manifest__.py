# -*- coding: utf-8 -*-
{
    'name': "res_partner_portal_task",
    'summary': """ Res Partner Portal Task """,
    'description': """ Res Partner Portal Task """,
    'author': "Fager Mohsen",
    'website': "http://www.github.com/fageer",
    'version': '0.1',
    'depends': ['base', 'contacts', 'portal', 'web'],
    'data': [
        'views/res_partner_view.xml',
        'views/res_partner_portal_form.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
}
