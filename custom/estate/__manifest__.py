{
    'name': 'Estate',
    'version': '',
    'summary': 'estate property module',
    'description': '',
    'depends':['base','mail'],
    'data':[
        'security/ir.model.access.csv',
        'wizard/delete_property_wizard_view.xml',
        'views/estate_property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/users_inherited_view.xml',
        'views/menu_view.xml',
        'report/estate_porperty_template.xml',
        'report/estate_property_report.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    }