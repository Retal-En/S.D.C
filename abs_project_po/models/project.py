# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2020-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import api, fields, models,_

class Project(models.Model):
    _inherit = 'project.project'

    purchase_order_ids = fields.One2many('purchase.order','project_id',string="Purchase Orders")
    po_count = fields.Integer(compute='compute_count')



    def get_po(self):
        self.ensure_one()
        proj_id= self.id 
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Orders',
            'view_mode': 'tree,form',
            'res_model': 'purchase.order',
            'domain': [('project_id', '=', self.id)],
            # 'context': "{'create': False,'edit'}"
            'context': "{'create': False,'edit':False}"
        }



    def create_po(self):
        self.ensure_one()
        proj_id= self.id 
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Orders',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'context': {'default_project_id': proj_id}
        }

    def compute_count(self):
        for record in self:
            record.po_count = self.env['purchase.order'].search_count(
                [('project_id', '=', self.id)])
