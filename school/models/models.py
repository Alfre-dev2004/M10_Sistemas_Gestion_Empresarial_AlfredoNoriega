# -*- coding: utf-8 -*-

from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Estudiante de la Escuela'

    # Requisitos básicos
    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    birth_date = fields.Date(string='Fecha de nacimiento')
    
    # Restricción de unicidad para el DNI
    dni = fields.Char(string='DNI/NIE', required=True)
    
    active = fields.Boolean(string='Activo', default=True)
    age = fields.Integer(string='Edad')

    # Relaciones
    # Un estudiante pertenece a una clase (Many2one)
    # Se deduce de la relación de agregación en el diagrama
    class_id = fields.Many2one('school.class', string='Clase')
    
    # Un estudiante puede asistir a muchos eventos (Many2many)
    # Definiremos la relación inversa aquí para comodidad, aunque el diagrama lo marca en Event
    event_ids = fields.Many2many('school.event', string='Eventos')

    # SQL Constraint para que el DNI sea único
    _sql_constraints = [
        ('dni_unique', 'unique(dni)', 'El DNI debe ser único.')
    ]


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
    _order = 'date