from odoo import api, fields, models


class PropertyType(models.Model):

    _name = 'property.type'
    _description = 'PropertyType is for mentioning the property type of each property'

    name = fields.Char(required=True)

