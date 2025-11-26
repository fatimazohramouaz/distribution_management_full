from odoo import models, fields, api
from datetime import date

class DistributionSaleOrder(models.Model):
    _name = 'distribution.sale.order'
    _description = 'Sale Order'

    name = fields.Char(string='Order Reference', default=lambda self: 'SO/%s' % date.today().strftime('%Y%m%d'))
    customer_id = fields.Many2one('distribution.client', string='Customer')
    order_date = fields.Date(default=fields.Date.context_today)
    order_line_ids = fields.One2many('distribution.sale.order.line', 'order_id', string='Order Lines')
    total_amount = fields.Monetary(compute='_compute_totals', store=True, currency_field='currency_id')
    paid_amount = fields.Monetary()
    remaining_debt = fields.Monetary(compute='_compute_totals', store=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')
    state = fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('done','Done')], default='draft')

    @api.depends('order_line_ids.quantity','order_line_ids.unit_price','paid_amount')
    def _compute_totals(self):
        for rec in self:
            total = 0.0
            for line in rec.order_line_ids:
                total += (line.quantity * line.unit_price)
            rec.total_amount = total
            rec.remaining_debt = total - (rec.paid_amount or 0.0)

    def action_confirm(self):
        # placeholder for stock reservation & state change
        for rec in self:
            rec.state = 'confirmed'
        return True

    def action_done(self):
        # placeholder for delivery / stock moves and marking done
        for rec in self:
            rec.state = 'done'
        return True

class DistributionSaleOrderLine(models.Model):
    _name = 'distribution.sale.order.line'
    _description = 'Sale Order Line'

    order_id = fields.Many2one('distribution.sale.order', string='Order Reference')
    product_id = fields.Many2one('distribution.product', string='Product')
    quantity = fields.Float(default=1.0)
    unit_price = fields.Monetary(currency_field='currency_id')
    subtotal = fields.Monetary(compute='_compute_subtotal', currency_field='currency_id')
    delivered_qty = fields.Float(default=0.0)
    currency_id = fields.Many2one('res.currency', string='Currency')

    @api.depends('quantity','unit_price')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = (rec.quantity or 0.0) * (rec.unit_price or 0.0)
