{
    'name': 'Create CV',
    'sequence': -105,
    'depends': ['base', 'mail', 'account', 'product', 'sale'],
    'author': 'Fager Mohsen',
    'summary': """ Create CV """,
    'description': """ Create CV """,
    'website': "https://fager-portfolio.vercel.app/",
    'version': '1.0.0',
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/create_cv_view.xml',
        'views/skills_tags_view.xml',
        'reports/report.xml',
        'reports/cv.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'

}
