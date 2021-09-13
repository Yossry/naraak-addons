
{
    'name': "Additional fields for Naraak",
    'version': "13.0.0.0",
    'summary': "additional fields",
    'category': 'Extra Addons',
    'description': """
        this app will add Account number field to chart of account
    """,
    'author': "Expertsintech",
    'website':"www.expertsintech.com",
    'depends': ['base', 'account'],
    'data': [
      'views/chart_of_account_view.xml',
       'views/altNameView.xml',
    ],
    'demo': [],
    "external_dependencies": {},
    "license": "AGPL-3",
    'installable': True,
    'auto_install': False,

}
