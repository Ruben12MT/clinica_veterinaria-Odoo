# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api

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
    age = fields.Integer(string='Edad', readonly=True, compute="_compute_age" )
    breed = fields.Char('Raza')
    notes = fields.Text('Notas')
    image = fields.Binary('Foto')
    agressive = fields.Boolean('Agresivo')
    birthday = fields.Date('Fecha de nacimiento', required=True)
    appointment_ids = fields.One2many('clinica.appointment', 'pet_id', string='Historial de citas', readonly=True)
    owner_id = fields.Many2one('clinica.owner', string='Dueño') 
    
    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthday:
                birth_date = fields.Date.from_string(record.birthday)
                years = today.year - birth_date.year
                anyoSupera = (today.month, today.day) < (birth_date.month, birth_date.day)
                record.age = years - int(anyoSupera)
            else:
                record.age = 0
