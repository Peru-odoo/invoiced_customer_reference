# -*- coding: utf-8 -*-
{
    'name': "Invoiced Customer Reference",
    'version': '1.2',
    'license': 'OPL-1',
    'category': 'Invoicing',
    'summary': ' Invoiced Customer Reference allows you to have the associated customer reference on each invoice line '
               'when creating a report. Ideal, when you want to combine two invoices.',
    'description': """
        -------------------------------------------------------------------------
        Allows you to have on each order line the associated customer reference.
        Ideal, when you want to combine two invoices.
        -------------------------------------------------------------------------
    """,
    'author': "Omydoo",
    'website': "https://www.omydoo.fr",
    'maintainer': 'Omydoo',
    'depends': ['base', 'sale_management'],
    'data': [
        # 'security/ir.model.access.csv',
        'reports/invoices_report_inherit.xml',
        'views/inherit_view_quotation_tree.xml',
        'views/inherit_view_bdc_tree.xml',
        'views/inherit_view_quotation_form.xml',
        'views/inherit_view_invoice_tree.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'active': False,
    'images': ['static/description/invoiced-ref-client-odoo-cover.gif'],
    'support': 'support@omydoo.fr',
    'price': 49.00,
    'currency': 'EUR',
}
