from odoo import models, fields, api
from datetime import date

class DistributionPurchaseOrder(models.Model):
    _name = 'distribution.purchase.order'
    _description = 'Purchase Order'

    name = fields.Char(string='PO Reference', default=lambda self: 'PO/%s' % date.today().strftime('%Y%m%d'))
    supplier_id = fields.Many2one('distribution.supplier', string='Supplier')
    order_date = fields.Date(default=fields.Date.context_today)
    order_line_ids = fields.One2many('distribution.purchase.order.line', 'order_id', string='Order Lines')
    total_amount = fields.Monetary(compute='_compute_totals', store=True, currency_field='currency_id')
    received = fields.Boolean(default=False)
    currency_id = fields.Many2one('res.currency', string='Currency')

    @api.depends('order_line_ids.quantity','order_line_ids.unit_price')
    def _compute_totals(self):
        for rec in self:
            total = 0.0
            for line in rec.order_line_ids:
                total += (line.quantity * line.unit_price)
            rec.total_amount = total

class DistributionPurchaseOrderLine(models.Model):
    _name = 'distribution.purchase.order.line'
    _description = 'Purchase Order Line'

    order_id = fields.Many2one('distribution.purchase.order', string='Order Reference')
    product_id = fields.Many2one('distribution.product', string='Product')
    quantity = fields.Float(default=1.0)
    unit_price = fields.Monetary(currency_field='currency_id')
    subtotal = fields.Monetary(compute='_compute_subtotal', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')

    @api.depends('quantity','unit_price')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = (rec.quantity or 0.0) * (rec.unit_price or 0.0)
