from odoo import models, fields, api
import logging

from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']    

    name = fields.Char(required=1,default="New",size=12)
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_availablity = fields.Date(tracking=1)
    # expected_price = fields.Float(digits=(0,5))
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute="_compute_diff",store=1,readonly=0)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage  = fields.Boolean()
    garden = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ],default='north')

    _sql_constraints = [
        ('unique_name','unique("name")','This name is already exists!'),
    ]

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    owner_address = fields.Char(related="owner_id.address",readonly=False)
    owner_phone = fields.Char(related="owner_id.phone",store=0)
    owner_phone_number = fields.Char(related="owner_id.phone", store=1, readonly=False)
    owner_phone_related = fields.Char(related="owner_id.phone", store=1, readonly=False)
    # owner_phone1 = fields.Char(related="owner_id.phone",store=0)

    state = fields.Selection([
        ("draft","Draft"),
        ("pending","Pending"),
        ("sold","Sold"),
    ],default="draft")

    # depends works with 'view fields' and relational filed
    @api.depends('expected_price','selling_price','owner_id.phone')
    def _compute_diff(self):
        for res in self:
            print('inside _compute_diff method')
            res.diff = res.expected_price - res.selling_price


    # onchange works with 'view fields only' and are inside the same form view
    # view fields are the field inside the same form view
    # means here we can not pass owner_id.phone as param like depends
    @api.onchange('expected_price')
    def _onchange_expacted_price(self):
        for res in self:
            print('inside _onchange_expacted_price method')
            return {
                'warning':{'title':'warning','message':'negative value.','type':'notification'}
            }

    @api.constrains('bedrooms')
    def _check_bedrooms_greter_than_zero(self):
        for res in self:
            if res.bedrooms < 0:
                print('not valid')  
                _logger.info("not valid")
                raise ValidationError('Plase add a valid value to bedrooms')
            

    @api.model_create_multi
    def create(self,vals):
        res = super(Property, self).create(vals)
        # res = super().create(self,vals)
        _logger.info("inside create method")
        #logic
        return res
    
    def action_draft(self):
        print('hello world error')
        for res in self:
            res.state = 'draft'
            # res.write({
            #     'state':'draft'
            # })
    def action_pending(self):
        print('hello world error')
        for res in self:
            res.state = 'pending'
            # res.write({
            #     'state':'pending'
            # })
    def action_sold(self):
        print('hello world error')
        for res in self:
            res.state = 'sold'
            # res.write({
            #     'state':'sold'
            # })



    
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None):
    #     res = super()._search(domain, offset, limit, order)
    #     _logger.info("inside search method")
    #     return res
    

    # def write(self, vals):
    #     res = super().write(vals)
    #     _logger.info("inside write method")
    #     return res
    
    # def unlink(self):
    #     res = super().unlink()
    #     _logger.info("inside unlink method")
    #     return res
            
    