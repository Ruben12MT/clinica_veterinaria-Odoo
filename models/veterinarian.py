# -*- coding: utf-8 -*-

from odoo import models, fields
#Hereda de Persona: Num Colegiado, Especialidad, Horario
class Veterinario(models.Model):
    _inherit = 'clinica.person'

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
