# -*- coding: utf-8 -*-

from odoo import models, fields


class TecnicoRecord(models.Model):

    _name = "tecnico.tecnico"
    # _rec_name = 'name'
    numero = fields.Char(string='Numero', readonly=True)
    name = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    telefono = fields.Char(string='Telefono', required=True)
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer')], string='Género')
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    activo = fields.Boolean(string='Activo', readonly=False, default=True)



class ClienteRecord(models.Model):

    _name = "cliente.cliente"
    numeroC = fields.Char(string='Numero de Servicio', readonly=True)
    fecha = fields.Date(string="Fecha del Servicio" , required=True)
    name = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    telefono = fields.Char(string='Telefono', required=True)
    calle = fields.Char(string='Calle', required=True)
    numero = fields.Integer(string='Numero', required=True)
    portal = fields.Char(string='Portal')
    escalera = fields.Char(string='Escalera')
    planta = fields.Char(string='Planta', required=True)
    puerta = fields.Char(string='Puerta', required=True)
    comentario = fields.Char(string='Comentario', required=True)
    asignado = fields.Many2one(comodel_name='tecnico.tecnico', string='Asignado')
    estado = fields.Selection([('p', 'Pendiente'), ('t', 'Terminado'), ('n', 'Nulo')], string='Estado', required=True)