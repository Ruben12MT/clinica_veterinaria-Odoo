# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Veterinarian(models.Model):
    _name = 'clinica.veterinarian'
    _inherits = {'clinica.person': 'person_id'}
    _description = 'Veterinario'

    license_number  = fields.Char(string='Número de Colegiado', required=True)
    specialty  = fields.Selection([
        ('dogs', 'Perros'),
        ('cats', 'Gatos'),
        ('birds', 'Pájaros'),
        ('reptiles', 'Reptiles'),
        ('others', 'Otros'),
    ], string='Especialidad', required=True)
    schedule = fields.Char(string='Horario')
    appointment_ids = fields.One2many('clinica.appointment', 'veterinarian_id', string='Historial de citas', readonly=True)
    state = fields.Selection([
        ('available', 'Disponible'),
        ('busy', 'En Consulta'),
        ('off', 'De Baja'),
    ], string='Estado', default='available', tracking=True)

    def action_set_busy(self):
        self.state = 'busy'

    def action_set_available(self):
        self.state = 'available'

    def action_set_off(self):
        self.state = 'off'

    @api.constrains('license_number')
    def _check_license_format(self):
        for record in self:
            if record.license_number and not record.license_number.startswith('LIC-'):
                raise ValidationError(
                    "Formato de licencia inválido: El número de colegiado debe "
                    "comenzar obligatoriamente por 'LIC-'. Ejemplo: LIC-12345"
                )