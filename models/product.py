from odoo import models, fields, api

class DistributionProduct(models.Model):
    _name = 'distribution.product'
    _description = 'Product for Distribution'
    _inherit = []

    name = fields.Char(required=True)
    default_code = fields.Char(string='Internal Reference')
    category = fields.Char()
    purchase_price = fields.Float()
    sale_price = fields.Float()
    quantity = fields.Float(string='Quantity on Hand')
    uom = fields.Char(string='Unit of Measure')
    low_stock = fields.Boolean(compute='_compute_low_stock')

    @api.depends('quantity')
    def _compute_low_stock(self):
        for rec in self:
            rec.low_stock = rec.quantity <= 5
