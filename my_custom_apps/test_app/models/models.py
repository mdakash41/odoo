# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError




class ResPartner(models.Model):
    _inherit = 'res.partner'

    # company_type = fields.Char("hello")
    company_type = fields.Selection(selection_add=[(
        'hospital', 'Hospital'
    )])

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


    def action_send_card(self):
        print('sending mail')
        template_id = self.env.ref('test_app.patient_card_email_template').id
        print("template id ",template_id)
        template = self.env['mail.template'].browse(template_id)
        print(template)
        template.send_mail(self.id, force_send=True)


    def name_get(self):
        res = []
        for field in self:
            res.append((field.id,'%s %s'%(field.name_seq,field.name)))
        return res

    @api.depends('name')
    def _compute_upper_name(self):
        for record in self:
            record.patient_name_upper = record.name.upper() if record.name else False

    def _inverse_upper_name(self):
        for record in self:
            record.name = record.patient_name_upper.lower() if record.patient_name_upper else False


    @api.depends('total_appointment')
    def get_total_appointment(self):
        total_app = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.total_appointment = total_app

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for record in self:
            if record.doctor_id:
                record.doctor_gender = record.doctor_id.gender

    @api.constrains('patient_age')
    def checkAge(self):
        for record in self:
            if record.patient_age < 5:
                raise ValidationError("Age should be greater than 5")

    def print_patient_card(self):
        print("hello from print patient card function")
        return self.env.ref('test_app.report_patient_card').report_action(self)

    name = fields.Char("Name", required=True)
    gender = fields.Selection([('male','Male'),('fe_male','Female')],default='male',string='Gender', track_visibility='always')
    patient_age = fields.Integer("Age", track_visibility='always',group_operator=False)
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default= lambda self:_('New'))
    age_group = fields.Selection(
        [
            ('major','Major'),
            ('minor','Minor')
        ],
        string="Age Group", compute="getAgeGroup",store=True
    )
    doctor_gender = fields.Selection(
        [
            ('male','Male'),
            ('femail','Female')
        ],
        string="Doctor Age",
    )
    total_appointment = fields.Integer(string="Toal Appointment", compute='get_total_appointment')
    active = fields.Boolean("Active",default=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    email_id = fields.Char(string="Email")
    user_id = fields.Many2one('res.users', string="PRO")
    patient_name_upper = fields.Char("Patient Name Upper",compute = '_compute_upper_name',inverse='_inverse_upper_name')


    @api.model
    def create(self, vals):
        if vals.get('name_seq',_('New'))==_('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
            result = super(HospitalPatient, self).create(vals)
            return result

    # def toggle_active(self):
    #     for record in self:
    #         record.active = not record.active

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

    def test_app(self):
        pass

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
