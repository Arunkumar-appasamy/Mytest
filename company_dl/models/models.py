# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Companydl(models.Model):
	_inherit='res.company'

	company_dl_one = fields.Char(string="DL Number 1")
	company_dl_two = fields.Char(string="DL Number 2")
	
