# -*- coding: utf-8 -*-

from odoo import http, models, fields, api

class libreria_categoria(models.Model):
      _name = "libreria.categoria"
      
      name = fields.Char(string="nombre",required=True,help="Introduce el nombre de la categoria")
      descripcion = fields.Text(string="descripcion")
      libros = fields.One2many("libreria.libro","categoria",string="libros")

class libreria_libro(models.Model):
      _name = "libreria.libro"

      name = fields.Char(string="Título",required=True)
      precio = fields.Float(string="precio")
      ejemplares = fields.Integer(string="ejemplares")
      fecha = fields.Date(String="Fecha de compra")
      segmano = fields.Boolean(string="Segunda mano")
      estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],string="Estado",default='0') 
      categoria = fields.Many2one("libreria.categoria",string="Categoria",required=True,ondelete="cascade")
      importetotal = fields.Float(string="Importe total",compute="_importetotal",store=True)

      @api.depends('precio','ejemplares')
      def _importetotal(self):
            for r in self:
                  r.importetotal = r.ejemplares*r.precio


# class libreria(models.Model):
#     _name = 'libreria.libreria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100