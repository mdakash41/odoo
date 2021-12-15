# -*- coding: utf-8 -*-
{
    'name': "test_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/appointment.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/sequence.xml',
        'reports/report.xml',
        'data/data.xml',
        'data/cron.xml',
        'data/mail_template.xml',
        'reports/patient_card.xml',
        'views/doctor.xml',
        'wizards/create_appointment.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
