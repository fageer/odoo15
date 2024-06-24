from odoo import api, fields, models, _

class StockRequest(models.Model):
    _name = "stock.request"
    _description = "Stock Request"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'
    
    
    ref = fields.Char(string='Referance', readonly=True)
    branch_id = fields.Many2one('branch.branch', string='Branch', required=True)
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('for_approval', 'For Approval'),
        ('confirmed', 'Confirmed')], string='Status', readonly=True, tracking=True)
    product_lines_ids = fields.One2many('product.lines', 'request_id', string='Product Lines')
    
    
    
    
    
    
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('stock.request')
        vals['state'] = 'draft'
        return super(StockRequest, self).create(vals)
    
    
    @api.onchange('branch_id')
    def _onchange_branch_id(self):
        self.warehouse_id = self.branch_id.warehouse_id.id
    
    
    def to_approval(self):
        print("Aprovallllllllllllllll ==================================================================")
        self.state = 'for_approval'
    
    def confirm(self):
        print("Confirmed ==================================================================")
        self.state = 'confirmed'
    
    
    
    
    
    
class ProductLines(models.Model):
    _name = "product.lines"
    _description = "Product Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default='1')
    request_id = fields.Many2one('stock.request', string='Request')