from odoo import models,fields,_,api


class CreateAppointment(models.Model):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient',string='Patient')
    appointment_date = fields.Date(string='Appointment Date')



    def create_appointment_object(self):
        vals = {
            'patient_id':self.patient_id.id,
            'appointment_date': self.appointment_date
        }

        self.env['hospital.appointment'].create(vals)
