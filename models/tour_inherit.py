from odoo import models, fields, api

class DistributionTour(models.Model):
    _inherit = 'distribution.tour'

    route_id = fields.Many2one('distribution.route', string='Route')

    @api.onchange('route_id')
    def _onchange_route(self):
        if self.route_id:
            lines = []
            for rl in self.route_id.route_line_ids.sorted(key=lambda r: r.sequence):
                lines.append((0, 0, {
                    'client_id': rl.client_id.id,
                    'expected_qty': rl.expected_qty,
                    'delivered_qty': 0.0,
                    'status': 'pending',
                }))
            self.tour_line_ids = lines
