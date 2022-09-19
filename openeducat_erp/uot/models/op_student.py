# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (c) 2022 Development Gateway, Inc and others.
#   
#    All rights reserved. This program and the accompanying materials
#    are made available under the terms of the MIT License (MIT)
#    which accompanies this distribution, and is available at
#    https://opensource.org/licenses/MIT
#   
#    Contributors:
#    Development Gateway - initial API and implementation
#
###############################################################################

from odoo import fields, models, api, _

class OpStudent(models.Model):
  _inherit = 'op.student'

  type_of_study = fields.Selection([
    ('u', 'Under graduate'),
    ('g', 'Graduate'),
    ('c', 'Post Graduate')
  ], 'Type of Study', required=True, default='u')

  start_year = fields.Date('Start year')

  @api.model
  def year_selection(self):
    year = 2000  # replace 2000 with your a start year
    year_list = []
    while year != 2030:  # replace 2030 with your end year
      year_list.append((str(year), str(year)))
      year += 1
    return year_list

  start_only_year = fields.Selection(
    year_selection,
    string="Start only year",
    default="2019",  # as a default value it would be 2019
  )
