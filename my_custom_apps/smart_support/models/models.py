# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tickets(models.Model):
    _name = 'support.tickets'
    _log_access = True
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'title'

    status = fields.Selection(string='Status', selection=[
        ('processing', 'Processing'),
        ('published', 'Published'),
        ('solved', 'Solved')
    ], default='processing')
    title = fields.Char(string="Title", required=True, )
    category = fields.Many2one('support.category')
    solved_date = fields.Datetime(String = "Issue Solved on")
    problem_description = fields.Text(string="Problem Description",groups="support_users_group")
    problem_solution = fields.Text(string= "Solution ",groups="support_technician_group")
    images = fields.Many2many('ir.attachment', string="Image")


class Category(models.Model):
    _name = 'support.category'

    name = fields.Char(string='Category Name', required = True)
    technician = fields.Many2one('res.partners', required = True)