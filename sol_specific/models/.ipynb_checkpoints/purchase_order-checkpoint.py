# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    # SOL_2023.01 - DEV-02-MO-PO-01 : L'estimate date est un champs lié à l'estimate date de la livraison  ou de la première livraision s'il y en a plusieur
    scheduled_date = fields.Date( string="Estimated date")
    # SOL_2023.01 - DEV-02-MO-PO-02 : L'effective date est un champs lié à l'effective date de la livraison  ou de la première livraision s'il y en a plusieur
    date_done = fields.Date( string="Effective date")


        
    


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    # " SOL_2023.01 - DEV-02-AC-01-01 : Purchase_order.py > StockPicking > change_po_schedule_date(self)
    #A partir d'un transfert ""copié"" sa schedule date dans le PO associé "
    def change_po_scheduled_date(self):
        _logger.info('------------------------')
        _logger.info('change_po_scheduled_date %s et %s', self.scheduled_date, self.date_done)
        _logger.info('------------------------')
        self.purchase_id.scheduled_date = self.scheduled_date
    
    #SOL_2023.01 - DEV-02-AC-01-02 : Purchase_order.py > StockPicking > change_po_date_done(self)
    #A partir d'un transfert ""copier"" son effective date dans le PO associé "
    def change_po_date_done(self):
        if self.purchase_id.date_done == False:
            self.purchase_id.date_done = self.date_done
        