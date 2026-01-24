# -*- coding: utf-8 -*-

from odoo import models, fields

class Person(models.Model):
    _name = 'clinica.person'
    _description = 'Persona'
    
    image = fields.Binary('Foto')
    name = fields.Char(string='Nombre', required=True)
    dni = fields.Char(string='DNI', required=True)
    phone = fields.Char(string='Teléfono')
    address = fields.Text(string='Dirección') 
