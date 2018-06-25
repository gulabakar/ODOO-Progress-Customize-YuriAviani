# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Component(models.Model):
    _name = 'comp.component'

    name = fields.Char(string="Nama Komponen", required=True)
    duration = fields.Integer('Durasi', default=1, required=True)

class Item(models.Model):
    _name = 'comp.item'

    name = fields.Char(string="Nama Item", required=True)
    component = fields.Many2one('comp.component', ondelete='cascade', string="Komponen", required=True)

class ComponentItem(models.Model):
    _name = 'comp.relation'

    comp = fields.One2many('comp.relation', 'component', string="Komponen")
    percentage = fields.Float(string="Percentase", compute='_com_percen')
    date = fields.Date()

    @api.depends('percen')
    def _com_percen(self):
        for r in self:
            if r.percen > 100:
                r.com_percen = 0.0
            else:
                r.com_percen = percen
                