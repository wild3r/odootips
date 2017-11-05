# -*- coding: utf-8 -*-
# Copyright 2017, Wilder Hernández García, Email: wilderhernandezg@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def name_get(self):
        if self._context is None:
            self._context = {}
        res = []
        if self._context.get('nombre_especial_para_mostrar', False):
            for partner in self:
                res.append((partner.id, ("%(parnter_order_count)s ventas - %(parnter_name)s") % {
                    'parnter_order_count': partner.sale_order_count,
                    'parnter_name': partner.name
                }))
        else:
            for record in self:
                res.append((record.id, ("%(parnter_name)s") % {
                    'parnter_name': record.name
                }))
        return res
