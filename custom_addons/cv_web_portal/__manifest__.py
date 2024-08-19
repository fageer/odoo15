{
    'name': 'CV Web Portal',
    'sequence': -105,
    'depends': ['base', 'create_cv', 'portal', 'web'],
    'author': 'Fager Mohsen',
    'summary': """ CV Web Portal """,
    'description': """ CV Web Portal """,
    'website': "https://fager-portfolio.vercel.app/",
    'version': '1.0.0',
    'data': [
        'views/portal_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'cv_web_portal/static/src/js/get_values.js',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
