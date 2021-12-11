from odoo import models,fields,api,_


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'


    @api.model
    def create(self, vals_list):
        if vals_list.get('name',_('New')) == _("New"):
            vals_list['name'] = self.env['ir.sequence'].next_by_code('hostpital.appointment') or _('New')
        result = super(HospitalAppointment, self).create(vals_list)
        return result

    name = fields.Char(string='Appointment ID', required = True, copy = False, readonly = True,
                       index = True, default= lambda self:_('New')
                       )
    patient_id = fields.Many2one('hospital.patient',string="Patient",required = True)
    patient_age = fields.Integer("Age", related='patient_id.patient_age')
    notes = fields.Text(String= 'Registration Note')
    appointment_date = fields.Date(string="Date",required=True)