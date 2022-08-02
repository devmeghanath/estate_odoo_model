from odoo import api, fields, models
from random import randint


class PropertyTag(models.Model):
    _name = 'property.tag'
    _description = 'PropertyTag'
    _order = "name"


    name = fields.Char(required=True)
    color = fields.Integer(
        string='Color',
        required=False)

