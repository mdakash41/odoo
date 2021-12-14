from odoo import models,fields


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctors Record"
    _rec_name = "name"

    name = fields.Char('Name',required=True)
    gender = fields.Selection([
        ('male', "Male"),
        ('female', 'Female')
    ], default='male', string="Gender")
    user_id = fields.Many2one('res.users', string="Related User")
