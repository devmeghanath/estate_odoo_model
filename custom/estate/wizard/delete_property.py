from odoo import api, fields, models


class DeleteProperty(models.TransientModel):
    _name = 'delete.property.wizard'
    _description = 'to delete property'

    property_id = fields.Many2one(
        comodel_name='estate.property',
        string='Property name',
        required=False)


    def delete_property(self):
        self.property_id.unlink()

        query = """ select id,name from estate_property """
        self.env.cr.execute(query)
        details = self.env.cr.dictfetchall()
        print('--------->',details)






