
{
    'name': 'OWL Partner Summary',
    'version': '1.0',
    'category': 'OWL',
    'author': 'Fager Mohsen',
    'sequence': -1,
    'summary': 'OWL Partner Summary',
    'description': """ OWL Partner Summary """,
    'depends': ['base', 'point_of_sale', 'web', 'pos_discount', 'sale_management'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_qweb': [
            'owl_partner_summary/static/src/xml/PartnerOrderSummary.xml',
        ],
        'web.assets_backend': [
            'owl_partner_summary/static/src/js/partnerorder.js',
        ],
    },
}
