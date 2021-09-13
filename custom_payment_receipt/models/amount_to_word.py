from odoo import api, fields, models
from datetime import datetime


class AccountPayment(models.Model):

    _inherit = 'account.payment'


    def _compute_amount_in_word(self):
        for rec in self:
            rec.num_word =  ' فقط '+ str(rec.currency_id.amount_to_text(rec.amount)) + ' لا غير '

    num_word = fields.Char(string="Amount In Words:", compute='_compute_amount_in_word')
