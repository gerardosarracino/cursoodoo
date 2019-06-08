# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryCategory(models.Model):
    _name = "library.category"

    name = fields.Char(string="Category")
    description = fields.Text(string="Description")
    book_id = fields.Many2one(comodel_name="library.book", string="Libro")

