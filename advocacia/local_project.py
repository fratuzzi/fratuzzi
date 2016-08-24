# -*- coding: utf-8 -*-
from openerp import models, fields
class LocalProject(models.Model):
    _name = 'local.project'
    _rec_name="local"
    local = fields.Char('Local', required=True)