from odoo import api, fields, models, _


class Advertiser(models.Model):
    _name = 'advertiser.advertiser'
    _description = "Advertiser"
    _rec_name = "advertiser_id"

    advertiser_id = fields.Many2one('res.partner', strring="Advertiser")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    advertisement_type_lines_ids = fields.One2many('advertisement.type.lines', 'advertiser_id', string='Advertisement Type Lines')

    @api.onchange('advertiser_id')
    def onchange_advertiser_id(self):
        for record in self:
            record.email = record.advertiser_id.email
            record.phone = record.advertiser_id.phone


class AdvertisementTypeLines(models.Model):
    _name = "advertisement.type.lines"
    _description = "Advertisement Type Lines"
    _rec_name = "advertiser_type"

    advertiser_type = fields.Char(string='Advertiser Type', required=True)
    percentage = fields.Integer(string='Percentage')
    advertiser_id = fields.Many2one('advertiser.advertiser', string='Advertiser')