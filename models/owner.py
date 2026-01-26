# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Owner(models.Model):
    _name = 'clinica.owner'
    _inherits = {'clinica.person': 'person_id'}
    _description = 'Dueño'

    bank_account = fields.Char(string='Cuenta Bancaria', required=True)
    debts = fields.Float(string='Deudas')
    pet_ids = fields.One2many('clinica.pet', 'owner_id', string='Mascotas', readonly=True)
    risk_level = fields.Selection([
        ('low', 'Bajo Riesgo'),
        ('medium', 'Riesgo Moderado'),
        ('high', 'Riesgo Alto')
    ], string='Nivel de Riesgo', compute='_compute_risk_level', store=True)

    @api.depends('debts', 'pet_ids')
    def _compute_risk_level(self):
        for record in self:
            num_pets = len(record.pet_ids)
            if record.debts > 200 or (record.debts > 100 and num_pets > 3):
                record.risk_level = 'high'
            elif record.debts > 0:
                record.risk_level = 'medium'
            else:
                record.risk_level = 'low'