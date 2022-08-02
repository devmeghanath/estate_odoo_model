from odoo import api, fields, models
class ResUser(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many(
        comodel_name='estate.property',
        inverse_name='user_id',
        string='Property ',
        required=False)


