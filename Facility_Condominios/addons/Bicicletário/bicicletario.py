from odoo import models, fields

class Bike(models.Model):
    _name = 'bicicletario.bike'
    _description = 'Bike'

    name = fields.Char(string='Nome')
    imagem = fields.Binary(string='Imagem')
    unidade = fields.Char(string='Unidade')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
