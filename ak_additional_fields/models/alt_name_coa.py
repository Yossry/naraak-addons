from odoo import models, api, _, _lt, fields

class COA_Page(models.Model):
    _inherit = 'account.account'

    account_number = fields.Char(string="Account Number")




