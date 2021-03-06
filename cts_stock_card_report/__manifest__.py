# Copyright 2019 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'cts Stock Card Report',
    'summary': 'Add stock card report on Inventory Reporting.',
    'version': '12.0.1.0.0',
    'category': 'Warehouse',
    'author': 'nadir',
    'license': 'AGPL-3',
    'depends': [
        'stock',
        'date_range',
        'report_xlsx_helper',
    ],
    'data': [
        'data/report_data.xml',
        'views/stock_card_report_tree.xml',
        'wizard/stock_card_report_wizard_view.xml',
    ],
    'installable': True,
}
