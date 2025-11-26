from odoo import models, fields, api

class DistributionClient(models.Model):
    _name = 'distribution.client'
    _description = 'Client (Customer)'

    name = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Related Partner')
    customer_type = fields.Selection([('gros','Gros'),('demi_gros','Demi-gros')], default='demi_gros')
    currency_id = fields.Many2one('res.currency', string='Currency')
    current_debt = fields.Monetary(currency_field='currency_id', compute='_compute_debt', store=True)
    sale_order_ids = fields.One2many('distribution.sale.order', 'customer_id', string='Sale Orders')
    debt_payment_ids = fields.One2many('distribution.debt.payment', 'client_id', string='Payments')

    @api.depends('sale_order_ids.total_amount','sale_order_ids.paid_amount')
    def _compute_debt(self):
        for rec in self:
            total = 0.0
            for so in rec.sale_order_ids:
                total += (so.total_amount - (so.paid_amount or 0.0))
            rec.current_debt = total

class DistributionSupplier(models.Model):
    _name = 'distribution.supplier'
    _description = 'Supplier'

    name = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Related Partner')
    vendor_code = fields.Char()
    currency_id = fields.Many2one('res.currency', string='Currency')
