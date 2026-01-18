# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Appointment(models.Model):
    _name = 'clinica.appointment'
    _description = 'Cita'
    
    name = fields.Char(string="Cita del", compute="_compute_name", store=True)    
    date = fields.Datetime(string="Fecha y Hora" ,required=True)
    reason = fields.Text(string="Razón") 
    state = fields.Selection([ 
            ('pending', 'Pendiente'), 
            ('done', 'Finalizada'), 
            ('cancelled', 'Cancelada'), 
            ], default='pending', string="Estado de la solicitud", readonly=True)
    color = fields.Integer(string='Color')
    pet_id = fields.Many2one('clinica.pet', string='Mascota')    
    
    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
            
    def action_draft(self):
        for record in self:
            record.state = 'pending'
    
    @api.depends('date') 
    def _compute_name(self): 
        for record in self: 
            if record.date: 
                local_date = fields.Datetime.context_timestamp(record, record.date)
                record.name = local_date.strftime("%Y-%m-%d %H:%M") 
            else: 
                record.name = "Appointment"