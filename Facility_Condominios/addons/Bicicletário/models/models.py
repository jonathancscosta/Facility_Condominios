from odoo import models, fields
class Bike(models.Model):
    _name = 'bicicletario.bike'
    _description = 'Modelo de Bicicleta'

    
class Bike(models.Model):
    _name = 'bicicletario.bike'
    _description = 'Modelo de Bicicleta'

class Bike(models.Model):
    _name = 'bicicletario.bike'
    _description = 'Modelo de Bicicleta'

    name = fields.Char(string='Identificação', required=True)
    image = fields.Binary(string='Imagem')
    unit = fields.Char(string='Unidade', required=True)
    brand = fields.Char(string='Marca', required=True)
    model = fields.Char(string='Modelo', required=True)

   