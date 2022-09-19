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

{
  'name': "University of Tikrit Extensions",
  'version': '1.0',
  'license': 'LGPL-3',
  'depends': ['hr', 'openeducat_core'],
  'author': "Octavian Ciubotaru",
  'category': 'Education',
  'description': "",
  'installable': True,
  'application': True,
  'data': [
    'views/hr_employee_views.xml',
    'views/op_student_views.xml'
  ],
  'assets': {
    'web.assets_backend': [
      '/uot/static/src/scss/style.scss'
    ]
  }
}
