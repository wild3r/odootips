# -*- coding: utf-8 -*-
# Copyright 2017, Wilder Hernández García, Email: wilderhernandezg@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cliente_total_sale_order = fields.Integer(
        string="Cantidad de ventas",
        compute="_compute_cliente_total_sale_order",
        search="_search_cliente_total_sale_order"
    )

    @api.one
    def _compute_cliente_total_sale_order(self):
        self.cliente_total_sale_order = self.partner_id.sale_order_count

    @api.model
    def _search_cliente_total_sale_order(self, operator, value):
        print self, operator, value
        res_ids = []
        objeto_ids = self.env['sale.order'].search([])
        for objeto in objeto_ids:
            qty_available = objeto._compute_cliente_total_sale_order()
            print qty_available
            if operator == '=':
                if qty_available == value:
                    res_ids.append(objeto.id)
            elif operator == '!=':
                if qty_available != value:
                    res_ids.append(objeto.id)
            elif operator == '>':
                if qty_available > value:
                    res_ids.append(objeto.id)
            elif operator == '<':
                if qty_available < value:
                    res_ids.append(objeto.id)
        return [('id', 'in', res_ids)]



