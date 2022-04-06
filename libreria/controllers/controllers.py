# -*- coding: utf-8 -*-
from odoo import http, models, fields, api

class libreria_categoria(models.Model):
      _name = "libreria.categoria"
      
      name = fields.Char(string="nombre",required=True,help="Introduce el nombre de la categoria")
      descripcion = fields.Text(string="Descripción")

class libreria_libro(models.Model):
      _name = "libreria.libro"

      name = fields.Char(string="Título",required=True)
      precio = fields.Float(string="Precio")
      ejemplares = fields.Integer(string="Ejemplares")
      fecha = fields.Date(String="Fecha de compra")
      segmano = fields.Boolean(string="Segunda mano")
      estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],string="Estado",default='0') 

# class Libreria(http.Controller):
#     @http.route('/libreria/libreria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libreria/libreria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('libreria.listing', {
#             'root': '/libreria/libreria',
#             'objects': http.request.env['libreria.libreria'].search([]),
#         })

#     @http.route('/libreria/libreria/objects/<model("libreria.libreria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libreria.object', {
#             'object': obj
#         })