# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import exceptions, fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _type_selection_list = [('none', 'NONE'),
                            ('rgt', 'RGT'),
                            ('spp', 'SPP'),
                            ('acc', 'ACC'),
                            ('ctl', 'CTL'),
                            ('cons', 'CONS'),
                            ('app', 'APP'),
                            ('cal', 'CAL'),
                            ('fluid', 'FLUID'),
                            ('ser', 'SER')]

    _famille_selection_list = [('none','NONE'),
                               ('eqas','EQAS'),
                               ('serology','SEROLOGIE'),
                               ('hematology','HEMATOLOGIE'),
                               ('microbiologie','Microbiologie'),
                               ('ia_ocd','IA OCD'),
                               ('groupage','GROUPAGE'),
                               ('ih','IH'),
                               ('hba1c','HBA1C'),
                               ('ai','AI'),
                               ('cc','CC'),
                               ('hemostase','HEMOSTASE'),
                               ('cc_ocd','CC OCD'),
                               ('biomol','BIOMOL'),
                               ('hla','HLA'),
                               ('ia&cc_ocd','IA&CC OCD'),
                               ('ic','IC'),('oncologie','Oncologie')]

    _temperature_selection_list = [('Ambiant', 'Ambiant'),
                                   ('2-8', '2-8 °C'),
                                   ('-20', '-20 °C'),
                                   ('-60', '-60 °C'),
                                   ('-80', '-80 °C')]
    product_type = fields.Selection(_type_selection_list, string='Type', default='none', store=True)
    cdt = fields.Char(string='CDT', store=True)
    temperatur_type = fields.Selection(_temperature_selection_list, string='Temperature', required=True, store=True)

    famille = fields.Selection(_famille_selection_list, string='Famille', default='none', store=True)

    quantity_pi = fields.Integer(string='Quantity PI', store=True)
    tarif_douane = fields.Char(string='Tarif Douanlier', store=True)
