# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class projectTeam(models.Model):
    _name='project.team'
    name = fields.Char()
    # poject_manager = fields.Many2one('res.users')
    team_leader = fields.Many2one('res.users')
    engineer_ids = fields.Many2many('res.users')

    company_id = fields.Many2one('res.company',default=lambda self: self.env.company.id)


