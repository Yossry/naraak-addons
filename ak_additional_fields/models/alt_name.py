from odoo import models, api, _, _lt, fields

class Partnerpage(models.Model):
    _inherit = 'res.partner'

    altName = fields.Char(string="English Name")
    partnerCode = fields.Char(string="Vendor Number" , index = True , store = True, required = False)




