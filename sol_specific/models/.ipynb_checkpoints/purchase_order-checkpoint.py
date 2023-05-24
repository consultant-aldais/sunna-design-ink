# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

     scheduled_date = fields.Date( string="Estimated date", related="picking_ids.scheduled_date")
     date_done = fields.Date( string="Effective date", related="picking_ids.date_done")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
