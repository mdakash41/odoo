from odoo import models,fields,_,api


class CreateAppointment(models.Model):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string='Appointment Date')

    def print_report(self):
        # print('hello there print_report function is called')
        # print('printing the self.env value\n', self.read()[0])
        # data = {
        #     'model':'create.appointment',
        #     'form':self.read()[0]
        # }
        #
        #  fixme: this function is not working correctly. need to fix this.
        # return self.env.ref('report').with_context(landscape=True).report_action(self, data=data)
        data = {
            'model': 'create.appointment',
            'form': self.read()[0]
        }
        # if data['form']['patient_id']:
        #     selected_patient = data['form']['patient_id'][0]
        #     appointments = self.env['hospital.appointment'].search([('patient_id', '=', selected_patient)])
        # else:
        #     appointments = self.env['hospital.appointment'].search([])
        # appointment_list = []
        # for app in appointments:
        #     vals = {
        #         'name': app.name,
        #         'notes': app.notes,
        #         'appointment_date': app.appointment_date
        #     }
        #     appointment_list.append(vals)
        # # print("appointments", appointments)
        # data['appointments'] = appointment_list
        # # print("Data", data)
        return self.env.ref('test_app.report_patient_card').with_context(landscape=True).report_action(self,
                                                                                                         data=data)

    def create_appointment_object(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': 'Created From The Wizard/Code'
        }
        self.patient_id.message_post(body="Appointment created successfully",
                                     subject="Appointment creation")
        #self.env['hospital.appointment'].create(vals)
        # creating appointments from the code
        new_appointment = self.env['hospital.appointment'].create(vals)
        context = dict(self.env.context)
        context['form_view_initial_mode'] = 'edit'
        return {'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'hospital.appointment',
                'res_id': new_appointment.id,
                'context': context
                }

    def delete_data_from_code(self):
        for record in self:
            record.patient_id.unlink()
            # print("Test",record)

    def get_data_from_db(self):
        appointments_result = self.env[
            'hospital.appointment'
        ].search([('patient_id','=',3)])
        for record in appointments_result:
            print('Appointment Name',record.name)
        print("hello fonm create_appointment py file")
       # FIXME: THIS IS TYPE IS NO WORKING IN THE ODOO14 VERSION
        # return {
        #     "type": "ir.actions.do_nothing"
        # }