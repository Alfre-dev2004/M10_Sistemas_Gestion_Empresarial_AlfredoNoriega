from odoo import models, fields, api

class GestionTareas(models.Model):
    _name = 'gestion.tareas'
    _description = 'Gestión de Tareas'

    nombre = fields.Char(string='Nombre', required=True)
    prioridad = fields.Integer(string='Prioridad', default=1)
    realizada = fields.Boolean(string='Realizada')
    urgente = fields.Boolean(string='Urgente', compute='_compute_urgente', store=True)

    @api.depends('prioridad')
    def _compute_urgente(self):
        for tarea in self:
            tarea.urgente = tarea.prioridad > 10
