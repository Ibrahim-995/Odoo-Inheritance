# -*- coding: utf-8 -*-
{
    'name': "DSL Prescription Report Extend",

    'summary': """
        DSL Prescription Report Extend""",

    'description': """
        It extends the DSL Prescription Report extension
    """,

    'author': 'Daffodil Software Limited',
    'support': 'https://daffodil-bd.com',
    'website': 'https://daffodil-bd.com',

    'category': 'Reports',
    'version': '0.1',

    'depends': ['base', 'dsl_hms_barcode', 'dsl_hms','dsl_prescription_extension'],

    'data': [
        'security/ir.model.access.csv',
        'views/prescription_order_inherit.xml',
        'views/chief_complain_view.xml',
        'views/hms_appointment_inherit.xml',
        'reports/report_prescription_order_extd.xml',
    ],
    
}
