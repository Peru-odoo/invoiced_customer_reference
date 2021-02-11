# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class meltingtrad_sequence(models.Model):
#     _name = 'meltingtrad.sequence'
#     _description = 'meltingtrad.sequence'

#     def sales_number_update(self, cr, uid, ids=None, context=None):
#         sequence_obj = self.pool.get('ir.sequence')
#         seq_id = sequence_obj.search(cr, uid, [('code', '=', 'sale.order')])
#         if seq_id:
#             value = sequence_obj.browse(cr, uid, seq_id[0])
#             number_next = value.number_next
#             sequence_obj.write(cr, uid, seq_id, {'number_next': 1})
#         return None
