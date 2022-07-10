from odoo import api, fields, models
import datetime

class PropertyOffer(models.Model):
    _name = 'property.offer'
    _description = 'PropertyOffer'

    create_date = fields.Date(
        string='Create date',
        required=False)

    price = fields.Float(
        string='Price', 
        required=False)
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'),
                   ('reffused', 'Reffused'), ],
        required=False,
        copy=False)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner_id',
        required=True)
    property_id = fields.Many2one(
        comodel_name='estate.property',
        string='Property_id',
        required=True)
    validity = fields.Integer(
        string='Validity',
        default=7,
        required=False)
    date_deadline = fields.Date(
        string='Date deadline',
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
        required=False)
    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date != False:
                record.date_deadline = (record.create_date + datetime.timedelta(days=record.validity))

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline != False:
                record.validity = (record.date_deadline - record.create_date).days


        

