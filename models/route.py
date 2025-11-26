from odoo import models, fields, api
from datetime import date

class DistributionZone(models.Model):
    _name = 'distribution.zone'
    _description = 'Geographical Zone'

    name = fields.Char(required=True)
    description = fields.Text()

class DistributionRoute(models.Model):
    _name = 'distribution.route'
    _description = 'Delivery Route'

    name = fields.Char(required=True)
    zone_id = fields.Many2one('distribution.zone', string='Zone')
    driver = fields.Char()
    vehicle = fields.Char()
    default_day = fields.Selection([('mon','Monday'),('tue','Tuesday'),('wed','Wednesday'),
                                    ('thu','Thursday'),('fri','Friday'),('sat','Saturday'),('sun','Sunday')],
                                   string='Default Delivery Day')
    route_line_ids = fields.One2many('distribution.route.line', 'route_id', string='Route Lines', copy=True)
    active = fields.Boolean(default=True)
    notes = fields.Text()

    def action_generate_tour(self):
        Tour = self.env['distribution.tour']
        TourLine = self.env['distribution.tour.line']
        created = []
        for route in self:
            tour_vals = {
                'name': '%s - %s' % (route.name, date.today().strftime('%Y%m%d')),
                'driver': route.driver,
                'vehicle': route.vehicle,
                'planned_date': date.today(),
                'notes': 'Generated from Route %s' % route.name,
            }
            tour = Tour.create(tour_vals)
            for line in route.route_line_ids.sorted(key=lambda r: r.sequence):
                TourLine.create({
                    'tour_id': tour.id,
                    'client_id': line.client_id.id,
                    'expected_qty': line.expected_qty,
                    'delivered_qty': 0.0,
                    'status': 'pending',
                })
            created.append(tour.id)
        return {'type':'ir.actions.act_window_close'}

class DistributionRouteLine(models.Model):
    _name = 'distribution.route.line'
    _description = 'Route Line (ordered client on a route)'

    route_id = fields.Many2one('distribution.route', string='Route', ondelete='cascade')
    sequence = fields.Integer(default=10)
    client_id = fields.Many2one('distribution.client', string='Client', required=True)
    client_address = fields.Char(related='client_id.partner_id.street', readonly=True)
    expected_qty = fields.Float(default=0.0)
    note = fields.Text()
    # simple map link (can be filled manually with Google Maps url)
    map_link = fields.Char(string='Map Link', help='Link to Google Maps or navigation for this client')
