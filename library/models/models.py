# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliotecaNombrelibro(models.Model):
    _name = "biblioteca.nombrelibros"

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")
    precio = fields.Float(string="Precio")
    ejemplares = fields.Integer(string="Ejemplares")
    fecha = fields.Date(string="Fecha")
    categoria = fields.Many2one("biblioteca.categoria", string="Categoria", required=True, ondelete="cascade")


class BibliotecaCategoria(models.Model):
    _name = "biblioteca.categoria"

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripcion")
    libros = fields.One2many("biblioteca.nombrelibros", "categoria", string="Libros")
