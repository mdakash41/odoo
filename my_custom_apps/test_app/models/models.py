# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals_list):
        res = super(ResPartner, self).create(vals_list)
        print(vals_list)
        return res

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string="Patient Name")

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Record"
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.depends('patient_age')
    def getAgeGroup(self):
        for record in self:
            if record.patient_age < 18:
                record.age_group = 'minor'
                return
            record.age_group = 'major'

    @api.depends('total_appointment')
    def get_total_appointment(self):
        total_app = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.total_appointment = total_app


    @api.constrains('patient_age')
    def checkAge(self):
        for record in self:
            if record.patient_age < 5:
                raise ValidationError("Age should be greater than 5")

    name = fields.Char("Name", required=True)
    gender = fields.Selection([('male','Male'),('fe_male','Female')],default='male',string='Gender', track_visibility='always')
    patient_age = fields.Integer("Age", track_visibility='always')
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default= lambda self:_('New'))
    age_group = fields.Selection(
        [
            ('major','Major'),
            ('minor','Minor')
        ],
        string="Age Group", compute="getAgeGroup"
    )
    total_appointment = fields.Integer(string="Toal Appointment", compute='get_total_appointment')
    active = fields.Boolean("Active",default=True)
    @api.model
    def create(self, vals):
        if vals.get('name_seq',_('New'))==_('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
            result = super(HospitalPatient, self).create(vals)
            return result

    def toggle_active(self):
        for record in self:
            record.active = not record.active

    def open_patients_appointment(self):
        return {
            'name':_('Appointments'),
            'domain':[('patient_id','=',self.id)],
            'view_type':'form',
            'res_model':'hospital.appointment',
            'view_id':False,
            'view_mode':'tree,form',
            'type':'ir.actions.act_window'
        }


# class test_app(models.Model):
#     _name = 'test_app.test_app'
#     _description = 'test_app.test_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
