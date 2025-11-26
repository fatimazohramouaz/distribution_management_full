from odoo import models, fields, api

class DistributionTour(models.Model):
    _name = 'distribution.tour'
    _description = 'Delivery Tour'

    name = fields.Char(required=True)
    driver = fields.Char()
    vehicle = fields.Char()
    client_ids = fields.Many2many('distribution.client', string='Clients')
    planned_date = fields.Date()
    tour_line_ids = fields.One2many('distribution.tour.line', 'tour_id', string='Tour Lines')
    notes = fields.Text()

class DistributionTourLine(models.Model):
    _name = 'distribution.tour.line'
    _description = 'Tour Line (clients on tour)'

    tour_id = fields.Many2one('distribution.tour', string='Tour')
    client_id = fields.Many2one('distribution.client', string='Client')
    expected_qty = fields.Float()
    delivered_qty = fields.Float(default=0.0)
    status = fields.Selection([('pending','Pending'),('delivered','Delivered'),('partial','Partial')], default='pending')

    def action_mark_delivered(self):
        for rec in self:
            rec.status = 'delivered'
