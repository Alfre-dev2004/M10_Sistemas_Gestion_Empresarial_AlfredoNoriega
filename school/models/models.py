# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Estudiante de la Escuela'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    birth_date = fields.Date(string='Fecha de nacimiento')

    dni = fields.Char(string='DNI/NIE', required=True)

    active = fields.Boolean(string='Activo', default=True)

    #  edad calculada
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)

    class_id = fields.Many2one('school.class', string='Clase')
    event_ids = fields.Many2many('school.event', string='Eventos')

    _sql_constraints = [
        ('dni_unique', 'unique(dni)', 'El DNI debe ser único.')
    ]

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.birth_date:
                b = rec.birth_date
                rec.age = today.year - b.year - ((today.month, today.day) < (b.month, b.day))
            else:
                rec.age = 0


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Clase de la Escuela'

    # Requisitos básicos
    name = fields.Char(string='Nombre de la clase', required=True) #
    grade = fields.Selection([
        ('first', 'Primero'),
        ('second', 'Segundo'),
        ('third', 'Tercero'),
        ('fourth', 'Cuarto')
    ], string='Grado') #
    
    date_begin = fields.Date(string='Fecha inicio')
    date_end = fields.Date(string='Fecha fin') # Deducido del diagrama "date_..."
    description = fields.Text(string='Descripción')
    student_number = fields.Integer(string='Número de estudiantes')

    # Relaciones
    # Tutor: Relación con el módulo de RRHH (hr.employee)
    tutor_id = fields.Many2one('hr.employee', string='Tutor')
    
    # Estudiantes: Relación inversa (One2many) hacia school.student
    student_ids = fields.One2many('school.student', 'class_id', string='Estudiantes')


class SchoolEvent(models.Model):
    _name = 'school.event'
    _description = 'Eventos Escolares'
    _order = 'date'

    date = fields.Date(string='Fecha', required=True)
    event_type = fields.Selection([
        ('trip', 'Excursión'),
        ('exam', 'Examen'),
        ('meeting', 'Reunión'),
        ('other', 'Otro'),
    ], string='Tipo de evento', required=True)

    description = fields.Text(string='Descripción')

    class_id = fields.Many2one('school.class', string='Clase')
    teacher_id = fields.Many2one('hr.employee', string='Profesor responsable')
    student_ids = fields.Many2many('school.student', string='Estudiantes')

    def name_get(self):
        result = []
        selection_map = dict(self._fields['event_type'].selection)

        for rec in self:
            tipo = selection_map.get(rec.event_type, '') if rec.event_type else ''
            clase = rec.class_id.name or ''
            display = f"{tipo} - {clase}".strip(" -")
            result.append((rec.id, display))
        return result