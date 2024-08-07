from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class StockRequest(models.Model):
    _name = "stock.request"
    _description = "Stock Request"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'

    ref = fields.Char(string='Referance', readonly=True)
    branch_id = fields.Many2one('branch.branch', string='Branch', required=True)
    location_id = fields.Many2one('stock.location', string='Location', required=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('for_approval', 'For Approval'),
        ('confirmed', 'Confirmed'),
        ('transfer', 'Transfer'),
        ('complete', 'Complete')], string='Status', readonly=True, tracking=True)
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
        self.location_id = self.branch_id.location_id.id

    def action_to_approval(self):
        responsible = self.branch_id.responsible_id.id
        if responsible == self.env.user.id:
            self.state = 'for_approval'
        else:
            raise ValidationError(_("You can't Approve The Request."))

    def action_confirm(self):
        is_inventory_admin = self.env.user.has_group('stock.group_stock_manager')
        if is_inventory_admin:
            self.state = 'confirmed'
        else:
            raise ValidationError(_("You can't Confirm The Request."))

    def action_transfer(self):
        is_inventory_admin = self.env.user.has_group('stock.group_stock_manager')
        if is_inventory_admin:
            picking_model = self.env['stock.picking']

            # Group product lines by stock_location_id
            product_lines_by_location = {}
            for line in self.product_lines_ids:
                if line.stock_location_id.id not in product_lines_by_location:
                    product_lines_by_location[line.stock_location_id.id] = []
                product_lines_by_location[line.stock_location_id.id].append(line)

            for location_id, lines in product_lines_by_location.items():
                move_vals = []
                move_line_vals = []

                for line in lines:
                    move_vals.append((0, 0, {
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.qty,
                        'product_uom': line.product_id.uom_id.id,
                        'name': line.product_id.name,
                        'location_id': line.stock_location_id.id,
                        'location_dest_id': self.location_id.id,
                    }))
                    move_line_vals.append((0, 0, {
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.qty,
                        'product_uom_id': line.product_id.uom_id.id,
                        'location_id': line.stock_location_id.id,
                        'location_dest_id': self.location_id.id,
                    }))

                picking_vals = {
                    'partner_id': self.branch_id.responsible_id.partner_id.id,
                    'picking_type_id': 29,
                    'location_id': location_id,
                    'location_dest_id': self.location_id.id,
                    'move_ids_without_package': move_vals,
                    'move_line_ids_without_package': move_line_vals
                }

                print(picking_vals)
                picking = picking_model.create(picking_vals)
                picking.action_confirm()

            self.state = 'complete'
        else:
            raise ValidationError(_("You can't Transfer The Request."))

    """Product Lines"""

class ProductLines(models.Model):
    _name = "product.lines"
    _description = "Product Lines"

    product_id = fields.Many2one('product.product', string='Product')  # Example field
    price_unit = fields.Float(related='product_id.list_price')
    stock_location_id = fields.Many2one('stock.location', string='Stock Location')
    request_id = fields.Many2one('stock.request', string='Request')
    is_created_po = fields.Boolean(string='po created', default=False)
    last_purchase_order_id = fields.Many2one('purchase.order', string='Last Purchase Order')
    qty = fields.Float(string='Quantity', default='1')  # Example field

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

    def action_purchase_order(self):
        if not self.product_id.seller_ids:
            raise ValidationError(_("This Product Don't Have Vendor."))

        purchase_order = self.env['purchase.order']
        self.is_created_po = True
        po_vals = {
                    'partner_id': self.product_id.seller_ids[0].name.id,
                    'date_order': fields.Date.today(),
                    'picking_type_id': 7,
                    'order_line': [(0, 0, {
                                    'product_id': self.product_id.id,
                                    'product_qty': self.qty,
                                    'price_unit': self.product_id.seller_ids[0].price,
                                    })],
                    }
        purchase_order.create(po_vals)
        print("=============================================Okkkkkkkkkkkkkkk", self.product_id.seller_ids[0].name.id)
        return {
                'effect': {
                            'fadeout': 'slow',
                            'message': 'Purchase Order Created Successfully',
                            'type': 'rainbow_man',
                            }
                }

