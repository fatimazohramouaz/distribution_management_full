from odoo import models, fields, api
from datetime import date

class DistributionDebtPayment(models.Model):
    _name = 'distribution.debt.payment'
    _description = 'Debt Payment by Client'

    name = fields.Char(string='Payment Ref', default=lambda self: 'PAY/%s' % date.today().strftime('%Y%m%d'))
    client_id = fields.Many2one('distribution.client', string='Client')
    payment_date = fields.Date(default=fields.Date.context_today)
    amount = fields.Monetary()
    currency_id = fields.Many2one('res.currency', string='Currency')
    note = fields.Text()

    def post_payment(self):
        # placeholder: in real use, create account.payment and reconcile
        return True
