from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MaterialKedatech(models.Model):
    _name = 'kedatech.material'
    _description = 'Material Client Kedatech'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection(
        [('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')],
        string='Material Type', required=True
    )
    material_buy_price = fields.Integer(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier', required=True)
