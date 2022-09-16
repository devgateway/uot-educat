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

from odoo import fields, models, _

class HrEmployee(models.Model):
  _inherit = 'hr.employee'

  height = fields.Integer("Height")
