from odoo import api, fields, models


class PropertyType(models.Model):

    _name = 'property.type'
    _description = 'PropertyType is for mentioning the property type of each property'
    _order = " sequence, name"

    name = fields.Char(required=True)
    property_ids = fields.One2many(
        comodel_name='estate.property',
        inverse_name='property_type_id',
        string='Property ids',
        required=False)
    sequence = fields.Integer('sequence', default=1)
    note_taker = fields.Html(
        string='Note taker',
        required=False)
    hide_name = fields.Boolean(
        string='Hide Name',

    )
    # offer_ids = fields.One2many(
    #     comodel_name='property.offer',
    #     inverse_name='property_type_id',
    #     string='Offer ids',
    #     required=False)

   
    offer_count = fields.Integer(
        string='Offer count',
        compute='_compute_offer_count',
        required=False)

    def _compute_offer_count(self):
        offer_count = self.env['property.offer'].search_count([('property_type_id','=',self.id)])
        self.offer_count = offer_count
    def offer_action(self):
        return {
            'name': 'offer_action_view',
            'view_mode': 'tree,form',
            'res_model': 'property.offer',
            'domain': [('property_type_id','=',self.id)],
            'res_id': self.id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'context': {}
        }


