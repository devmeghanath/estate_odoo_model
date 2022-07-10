from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'EstateProperty model for managing properties'


    property_type_id = fields.Many2one(
        comodel_name='property.type',
        string='Property Type',
        required=False)
    property_tag_ids = fields.Many2many(
        comodel_name='property.tag',
        string='Property_tag_ids')
    offer_ids = fields.One2many(
        comodel_name='property.offer',
        inverse_name='property_id',
        string='Offers',
        required=False)

    id = fields.Integer(
        string='Id',
        required=True)
    create_uid = fields.Integer(
        string='uid',
        required=False)
    create_date = fields.Date(
        string='Created date',
        required=False)
    write_uid = fields.Integer(
        string='Write uid',
        required=False)
    write_date = fields.Date(
        string='Write Date',
        required=False)
    name = fields.Char(
        string='Name',
        required=True)
    description = fields.Text(
        string="Description",
        required=False)
    postcode = fields.Char(
        string='Postcode',
        required=False)
    available_from = fields.Date(
        string='Available from',
        default=lambda self:date.today(),
        required=False)
    date_availability = fields.Date(
        string='Date_availability',
        default=lambda self: date.today() + relativedelta(months=+3),
        copy=False,
        required=False)
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=False)

    expected_price = fields.Monetary(
        'Expected Price',
        required=True
    )
    selling_price = fields.Monetary(
        'Selling Price',
        readonly=True,
        copy=False
    )
    bedrooms = fields.Integer(
        string='Bedrooms',
        default=2,
        required=False)
    living_area = fields.Integer(
        string='Living Area',
        required=False)
    facades = fields.Integer(
        string='Facades',
        required=False)

    garage = fields.Boolean(
        string='Garage',
        required=False)
    garden = fields.Boolean(
        string='Garden',
        required=False)
    garden_area = fields.Integer(
        string='Garden Area',
        required=False)
    garden_orientation = fields.Selection(
        [('north','North'),('east','East'),('west','West'),('south','South')],
        string='Garden Orientation',
        required=False)
    active = fields.Boolean(
        default=True,
        string='Active',
        required=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'),
                   ('offer_accepted', 'Accept'),
                   ('offer_received','Received'),
                   ('sold','Sold'),
                   ('cancelled','Cancelled')],
        default='new',
        required=True, )
    buyer = fields.Char(
        string='Buyer',
        required=False,
        copy=False)
    sales_person = fields.Char(
        string='Sales Person',
        default= lambda self:self.env.user.name,
        required=False)
    total_area = fields.Float(
        string='Total Area',
        compute="_compute_total_area",
        required=False)
    best_price = fields.Float(
        string='Best price',
        compute='_compute_best_price',
        required=False)


    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        self.total_area = self.living_area+self.garden_area


    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            try:
                record.best_price = max(record.offer_ids.mapped('price'))
            except ValueError:
                record.best_price = 0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation='north'
        else:
            self.garden_area=0
            self.garden_orientation=None







