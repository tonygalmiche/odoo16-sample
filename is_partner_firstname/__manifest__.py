{
    'name': 'Partner Firstname',
    'version': '16.0.1.0.0',
    'category': 'Contact',
    'summary': 'Add firstname field to res.partner',
    'description': """
        This module adds a firstname field to the partner model (res.partner).
        The firstname will be displayed in the partner form view.
    """,
    'author': 'Tony Galmiche',
    'website': 'https://github.com/tonygalmiche/odoo16-sample',
    'license': 'GPL-3',
    'depends': ['base'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}