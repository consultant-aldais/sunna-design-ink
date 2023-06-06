# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import logging

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    # SOL_2023.01 - DEV-02-MO-PO-01 : L'estimate date est un champs lié à l'estimate date de la livraison  ou de la première livraision s'il y en a plusieur
    scheduled_date = fields.Date( string="Estimated date")
    # SOL_2023.01 - DEV-02-MO-PO-02 : L'effective date est un champs lié à l'effective date de la livraison  ou de la première livraision s'il y en a plusieur
    date_done = fields.Date( string="Effective shipment date")


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    # " SOL_2023.01 - DEV-02-AC-01-01 : Purchase_order.py > StockPicking > change_po_schedule_date(self)
    #A partir d'un transfert ""copié"" sa schedule date dans le PO associé "
    def change_po_scheduled_date(self):
        _logger.info('------------------------')
        _logger.info('change_po_scheduled_date %s et %s', self.sale_id, self.scheduled_date)
        _logger.info('------------------------')
        self.purchase_id.scheduled_date = self.scheduled_date
    
    #SOL_2023.01 - DEV-02-AC-01-02 : Purchase_order.py > StockPicking > change_po_date_done(self)
    #A partir d'un transfert ""copier"" son effective date dans le PO associé. "

    def change_po_date_done(self):
        aged_effective_date = datetime.date(2000, 1, 1)
        _logger.info('------------------------')
        _logger.info('change_po_date_done')
        _logger.info('------------------------')
        for transfert in self.purchase_id.picking_ids:
            _logger.info('------------------------')
            _logger.info('change_po_date_done %s et %s', transfert.effective_shipment_date, aged_effective_date)
            _logger.info('------------------------')
            if (transfert.effective_shipment_date is not False):
                if (transfert.effective_shipment_date > aged_effective_date):
                    aged_effective_date = transfert.effective_shipment_date
        self.purchase_id.date_done = aged_effective_date
        #self.purchase_id.date_done = self.effective_shipment_dat
        