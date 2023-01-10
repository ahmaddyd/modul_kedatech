from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Supplier(models.Model):
    _inherit = 'res.partner'

    related_supplier = fields.Boolean(string='Supplier', default=False)
