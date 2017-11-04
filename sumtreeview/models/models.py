# -*- coding: utf-8 -*-
# Copyright 2017, Wilder Hernández García, Email: wilderhernandezg@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None,
                   orderby=False, lazy=True):
        res = super(SaleOrder, self).read_group(domain, fields, groupby,
            offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        if 'amount_tax' in fields:
            for line in res:
                if '__domain' in line:
                    total_amount_tax = 0.0
                    lines = self.search(line['__domain'])
                    for item in lines:
                        total_amount_tax += item.amount_tax
                    line['amount_tax'] = total_amount_tax
        return res

