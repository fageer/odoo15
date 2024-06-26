from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


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
    branch_responsible_id = fields.Many2one(
        'res.users', 
        string="Branch Responsible", 
        related='branch_id.responsible_id', 
        store=True
    )
    is_responsible_user = fields.Boolean(
        string="Is Responsible User",
        compute="_compute_is_responsible_user",
        default=False,
        store=False
    )
    
    



    @api.depends('branch_responsible_id')
    def _compute_is_responsible_user(self):
        for record in self:
            record.is_responsible_user = record.branch_responsible_id.id == self.env.user.id
    
    
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('stock.request')
        vals['state'] = 'draft'
        return super(StockRequest, self).create(vals)
    
    
    @api.onchange('branch_id')
    def _onchange_branch_id(self):
        self.warehouse_id = self.branch_id.warehouse_id.id
    
    
    def to_approval(self):
        responsible = self.branch_id.responsible_id.id
        if responsible == self.env.user.id:
            self.state = 'for_approval'
        else:
            raise ValidationError(_("You can't Approve The Request."))
            return
            

    def confirm(self):
        is_inventory_admin = self.env.user.has_group('stock.group_stock_manager')
        if is_inventory_admin:
            self.state = 'confirmed'
        else:
            raise ValidationError(_("You can't Confirm The Request."))
            return
    
    
    
    
    
class ProductLines(models.Model):
    _name = "product.lines"
    _description = "Product Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default='1')
    stock_location_id = fields.Many2one('stock.location', string='Stock Location')
    request_id = fields.Many2one('stock.request', string='Request')
    
    
    
    def action_forcast(self):
        self.ensure_one()  
        action = self.env.ref('branch_task.action_forcast_stock').read()[0]
        action['context'] = {
            'default_product_id': self.product_id.id,
        }
        # self.stock_location_id = action['context']['default_product_id'].location_id.id
        action['domain'] = [('product_id', '=', self.product_id.id)]
        if not action['domain']:
            print("No Available Quantity ===========================================================", action['domain'])
        else:
            print("Available Quantity ===========================================================", action['domain'])
        return action