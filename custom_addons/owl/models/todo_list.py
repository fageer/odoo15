from odoo import api, fields, models, _


class OwlTodo(models.Model):
    _name = "owl.todo.list"
    _description = "Owl Todo List App"

    name = fields.Char(string='Name')
    completed = fields.Boolean()
    color = fields.Char()
