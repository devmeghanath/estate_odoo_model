from odoo import api, fields, models

class PropertyTag(models.Model):
    _name = 'property.tag'
    _description = 'PropertyTag'

    name = fields.Char(required=True)

