from odoo import models

class PateintCardXLS(models.AbstractModel):
    _name = 'report.test_app.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 14,'align': 'center','bold': True})
        sheet = workbook.add_worksheet('Patient Card')
        # sheet_column increase the size of the column.
        # in this example we seet the row 2 and column 3 with size 50
        sheet.set_column(2,3,50)
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, lines.name, format1)
