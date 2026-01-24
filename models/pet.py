# -*- coding: utf-8 -*-

from odoo import models, fields

class Pet(models.Model):
    _name = 'clinica.pet'
    _description = 'Mascota'
    
    name = fields.Char(string='Nombre', required=True)
    species = fields.Selection([
        ('dog', 'Perro'),
        ('cat', 'Gato'),
        ('bird', 'Pájaro'),
        ('reptile', 'Reptil'),
        ('other', 'Otro'),
    ], string='Especie', required=True)
    age = fields.Integer(string='Edad')
    breed = fields.Char('Raza')
    notes = fields.Text('Notas')
    image = fields.Binary('Foto')
    agressive = fields.Boolean('Agresivo')
    birthday = fields.Date('Fecha de nacimiento')
    appointment_ids = fields.One2many('clinica.appointment', 'pet_id', string='Historial de citas', readonly=True)
    owner_id = fields.Many2one('clinica.owner', string='Dueño')    
