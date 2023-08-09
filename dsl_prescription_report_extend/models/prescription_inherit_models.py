# -*- coding: utf-8 -*-

from odoo import fields, models

class ChiefComplain(models.Model):
    _name = 'chief.complain'
    _description = 'Chief Complain'

    name = fields.Char(string='Complain', required=True)
    note = fields.Char(string='Notes')


class PrescriptionOrder(models.Model):
    _inherit = 'prescription.order'

    chief_complain_extd = fields.Many2many('chief.complain',string='Chief Complain')
    weight = fields.Float(string='Weight (kg)', default=0.00)
    systolic_bp_extd = fields.Char(string="Systolic BP", size=3)
    diastolic_bp_extd = fields.Char(string="Diastolic BP", size=3)
    age_extd = fields.Char(string= "Age")


class PrescriptionOrder(models.Model):
    _inherit = 'hms.appointment'

    chief_complain_extd = fields.Many2many('chief.complain',string='Chief Complain')


