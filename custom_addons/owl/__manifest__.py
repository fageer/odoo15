
{
    'name': 'OWL Tutorial',
    'version': '1.0',
    'category': 'OWL',
    'author': 'Fager Mohsen',
    'sequence': -1,
    'summary': 'OWL Tutorial',
    'description': """ OWL Tutorial """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'owl/static/src/components/*/*.js',
            'owl/static/src/components/*/*.xml',
            'owl/static/src/components/*/*.scss',
        ],
    },
}
