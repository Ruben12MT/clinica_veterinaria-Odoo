# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Appointment(models.Model):
    _name = 'clinica.appointment'
    _description = 'Cita'
    
    name = fields.Char(string="IDENTIFICADOR", compute="_compute_name", store=True)    
    date = fields.Datetime(string="Fecha y Hora" ,required=True)
    reason = fields.Text(string="Razón") 
    state = fields.Selection([ 
            ('pending', 'Pendiente'), 
            ('done', 'Finalizada'), 
            ('cancelled', 'Cancelada'), 
            ], default='pending', string="Estado de la solicitud", readonly=True)
    color = fields.Integer(string='Color')
    urgency = fields.Boolean(string='¿Es una urgencia?')

    pet_id = fields.Many2one('clinica.pet', string='Mascota')    
    veterinarian_id = fields.Many2one('clinica.veterinarian', string='Veterinario asignado')
    appointment_ids = fields.One2many('clinica.appointment', 'pet_id', string='Historial de citas', readonly=True)
    treatment_ids = fields.Many2many('clinica.treatment', string='Tratamientos')

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
            
    def action_draft(self):
        for record in self:
            record.state = 'pending'
    
    @api.depends('date', 'urgency') 
    def _compute_name(self): 
        for record in self: 
            if record.date: 
                urgencia = ""
                if(record.urgency):
                    urgencia = "_URG"
                local_date = fields.Datetime.context_timestamp(record, record.date)
                record.name = "APPT_" + local_date.strftime("%Y-%m-%d_%H-%M") + str(urgencia)
            else: 
                record.name = "Appointment"