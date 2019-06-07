# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book")
    description = fields.Text(string="Description")
    category_ids = fields.One2many(comodel_name="library.category",
                                   inverse_name="book_id",
                                   string="Categorias")
