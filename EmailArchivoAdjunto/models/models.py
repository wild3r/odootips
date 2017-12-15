# -*- coding: utf-8 -*-
# Copyright 2017, Wilder Hernández García, Email: wilderhernandezg@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='attachments_rel',
        column1='account_id',
        column2='attachment_id',
        string='Archivo Adjunto'
    )


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def onchange_template_id(self,
                             template_id,
                             composition_mode,
                             model,
                             res_id):
        r = super(MailComposer, self).onchange_template_id(template_id,
                                                           composition_mode,
                                                           model,
                                                           res_id)
        ai_id = self._context['active_ids'][0]
        ids = []
        for line in self.env['account.invoice'].search([('id', '=', ai_id)]):
            for lines_attachment in line.attachment_ids:
                ids.append(lines_attachment.id)
        if r['value']['attachment_ids']:
            ids.insert(0, r['value']['attachment_ids'][0])
            r['value']['attachment_ids'] = ids
        return r
