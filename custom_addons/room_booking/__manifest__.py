{
    'name': 'Room Booking',
    'sequence': -102,
    'depends': ['mail'],
    'author': 'Plus Tech',
    'summary': """ Room Booking """,
    'description': """ Room Booking """,
    'website': "http://www.plustech.com",
    'version': '1.0.0',
    'data':[
        'security\ir.model.access.csv',
        'views/menu.xml',
        'views/facility_room_view.xml',
        'views/room_view.xml',
        'views/booking_room_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'

}
