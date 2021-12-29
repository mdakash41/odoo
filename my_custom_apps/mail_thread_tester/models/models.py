# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mail_thread_tester(models.Model):
    _name = 'test.mail_thread'
    _description = 'Mail Thread tester'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char('Name Filed', required=True,track_visibility='always')
    image = fields.Many2many('ir.attachment', string="Image")
