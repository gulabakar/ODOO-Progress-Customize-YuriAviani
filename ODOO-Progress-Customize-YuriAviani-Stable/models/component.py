# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Component(models.Model):
    _name = 'comp.component'
    
    name = fields.Char(string="Nama Komponen", required=True)
    duration = fields.Integer('Durasi', default=1, required=True)
