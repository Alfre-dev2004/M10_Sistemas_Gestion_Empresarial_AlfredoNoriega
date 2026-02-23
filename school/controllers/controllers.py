from odoo import http
from odoo.http import request


class SchoolController(http.Controller):

    @http.route('/school/events/', auth='public', type='http', website=True)
    def list_events(self, **kwargs):
        events = request.env['school.event'].sudo().search([])
        lines = [ev.display_name for ev in events]  # usa name_get

        return "<br/>".join(lines) if lines else "No hay eventos"