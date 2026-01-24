# -*- coding: utf-8 -*-

from odoo import models, fields

class Treatment(models.Model):
    _name = 'clinica.treatment'
    _description = 'Tratamiento'
    
    name = fields.Char(string='Nombre', required=True)
    appointment_ids = fields.Many2many('clinica.appointment', string='Citas')
