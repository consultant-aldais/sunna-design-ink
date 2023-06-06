# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
import datetime
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    #SOL_2023.01 -  DEV-03-MO-SO-01 : L'estimate date est un champs lié à l'estimate date de la livraison  ou de la première livraision s'il y en a plusieur
    scheduled_date = fields.Date( string="Estimated date")
    #SOL_2023.01 -  DEV-03-MO-SO-02 : L'effective date est un champs lié à l'effective date de la livraison  ou de la première livraision s'il y en a plusieur    
    date_done = fields.Date( string="Effective shipment date")


        
    


class StockPicking(models.Model):
    _inherit = 'stock.picking'
     
    #SOL_2023.01 - DEV-02-MO-SP-01 : Ajouter effective shipment date, manuellemet modifiable
    effective_shipment_date = fields.Date( string="Effective shipment date")

    #" SOL_2023.01 -  DEV-03-AC-01-01 : sale_order.py > StockPicking > change_so_schedule_date(self) A partir d'un transfert ""copié"" sa schedule date dans le PO associé "
     # SOL_2023.01 -  DEV-03-MO-SO-03 :  Dans le cas où il y ait plusieurs étapes de transfert (exemple avec ORD050764) avec des Schedule date différentes, l’Estimated Ship Date qui apparait dans la vue liste doit être la date la plus éloignée,
    def change_so_scheduled_date(self):  
        aged_effective_date = datetime.datetime(2000, 1, 1)
        _logger.info('------------------------')
        _logger.info('change_so_date_shedule')
        _logger.info('------------------------')
        for transfert in self.sale_id.picking_ids:
            _logger.info('------------------------')
            _logger.info('change_so_date_schedule %s et %s', transfert.scheduled_date, aged_effective_date)
            _logger.info('------------------------')
            if (transfert.scheduled_date is not False):
                if (transfert.scheduled_date > aged_effective_date):
                    aged_effective_date = transfert.scheduled_date
        self.sale_id.scheduled_date = aged_effective_date
        #self.sale_id.scheduled_date = self.scheduled_date
    
    #" SOL_2023.01 -  DEV-03-AC-01-02 : sale_order.py > StockPicking > change_so_date_done(self) A partir d'un transfert ""copier"" son effective date dans le PO associé "
    # SOL_2023.01 -  DEV-03-MO-SO-04 :  Dans le cas où il y ait plusieurs étapes de transfert (exemple avec ORD050764) avec 
    #des    effective ship date différentes, l’effective ship Date qui apparait dans la vue liste doit être la date la plus 
    #éloignée
    def change_so_date_done(self):
        aged_effective_date = datetime.date(2000, 1, 1)
        _logger.info('------------------------')
        _logger.info('change_so_date_done')
        _logger.info('------------------------')
        for transfert in self.sale_id.picking_ids:
            _logger.info('------------------------')
            _logger.info('change_so_date_done %s et %s', transfert.effective_shipment_date, aged_effective_date)
            _logger.info('------------------------')
            if (transfert.effective_shipment_date is not False):
                if (transfert.effective_shipment_date > aged_effective_date):
                    aged_effective_date = transfert.effective_shipment_date
        self.sale_id.date_done = aged_effective_date
        #self.sale_id.date_done = self.effective_shipment_date
    
    #     " SOL_2023.01 -  DEV-03-AC-02-04 : Création d'une action automatisée Z_AA_Update effective shipment date
    # L'action se décelnche lorque l'effective date est modifié dans la livraison
    # L'action se décelnche pour tous les type de livraison"
    def copy_date_done_effective_date(self):
        if (self.effective_shipment_date is False):
            self.effective_shipment_date = self.date_done 