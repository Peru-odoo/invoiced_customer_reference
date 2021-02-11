# -*- coding: utf-8 -*-

from odoo import models, fields, api, osv


class sale_order(models.Model):
    _inherit = 'sale.order'

    client_order_ref = fields.Char(string="Reference Client")


class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    client_ref = fields.Char(related="order_id.client_order_ref")

    # Method pour envoyer le champs vers invoice line
    def _prepare_invoice_line(self, sequence=False):
        # Récupération des anciennes valeures
        res = super(sale_order_line, self)._prepare_invoice_line()
        # Ajout/modification de la new valeur
        res.update({'client_ref': self.client_ref})
        return res


class account_move_line(models.Model):
    _inherit = 'account.move.line'

    client_ref = fields.Char(string="Reference Client", readonly=True)
