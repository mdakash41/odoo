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

        self.patient_id.message_post(body="Test String ",subject='Appointment Creation')
        self.env['hospital.appointment'].create(vals)

    def get_data_from_db(self):
        appointments_result = self.env[
            'hospital.appointment'
        ].search([('patient_id','=',3)])
        for record in appointments_result:
            print('Appointment Name',record.name)