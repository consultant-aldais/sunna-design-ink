# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    #SOL_2023.01 -  DEV-03-MO-SO-01 : L'estimate date est un champs lié à l'estimate date de la livraison  ou de la première livraision s'il y en a plusieur
    scheduled_date = fields.Date( string="Estimated date")
    #SOL_2023.01 -  DEV-03-MO-SO-02 : L'effective date est un champs lié à l'effective date de la livraison  ou de la première livraision s'il y en a plusieur    
    date_done = fields.Date( string="Effective date")


        
    


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    #" SOL_2023.01 -  DEV-03-AC-01-01 : sale_order.py > StockPicking > change_so_schedule_date(self) A partir d'un transfert ""copié"" sa schedule date dans le PO associé "
    def change_so_scheduled_date(self):
       
        # _logger.info('------------------------')
        # _logger.info('change_so_scheduled_date %s et %s', self.sale_id, self.scheduled_date)
        # _logger.info('------------------------')
        self.sale_id.scheduled_date = self.scheduled_date
    
    #" SOL_2023.01 -  DEV-03-AC-01-02 : sale_order.py > StockPicking > change_so_date_done(self) A partir d'un transfert ""copier"" son effective date dans le PO associé "
    def change_so_date_done(self):
        if self.sale_id.date_done == False:
            # _logger.info('------------------------')
            # _logger.info('change_so_date_done %s et %s', self.scheduled_date, self.date_done)
            # _logger.info('------------------------')
            self.sale_id.date_done = self.date_done