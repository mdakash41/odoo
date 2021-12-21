from odoo import models,fields,api


class PatientCardReport(models.Model):
    _name = 'report.test_app.report_patient'
    _description = "Patient Card Report"

    @api.model
    def _get_report_values(self, docids, data=None):

        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.patient'].search([('id','=',docids[0])])
        appointment_list =[]
        for vals in appointments:
            val = {
                "name":vals.name,
                "notes":vals.notes,
                "upper_name":vals.patient_name_upper,
            }
            appointment_list.append(val)

        return {
            'doc_model': 'hospital.patient',
            'docs': docs,
            'data': data,
            "appointment_list":appointment_list
        }