# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book")
    description = fields.Text(string="Description")
    isbn = fields.Char("ISBN")
    category_ids = fields.One2many(comodel_name="library.category",
                                   inverse_name="book_id",
                                   string="Categorias")

    _sql_constraints = [('name_uniq', 'unique (name)', """Book name should be unique!"""),]

    categ_count = fields.Integer(string="Nro categorias", compute="_count_categ")

    def _count_categ(self):
        for book in self:
            book.categ_count = len(book.category_ids)

    @api.constrains("isbn")
    def check_isbn(self):
        isbn = self.search([['id', '!=', self.id]]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError("ISBN duplicado")
