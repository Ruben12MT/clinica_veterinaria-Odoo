# -*- coding: utf-8 -*-

from odoo import models, fields

class Owner(models.Model):
    _name = 'clinica.owner'
    _inherits = {'clinica.person': 'person_id'}
    _description = 'Dueño'

    bank_account = fields.Char(string='Cuenta Bancaria', required=True)
    debts = fields.Float(string='Deudas')
    pet_ids = fields.One2many('clinica.pet', 'owner_id', string='Mascotas', readonly=True)
