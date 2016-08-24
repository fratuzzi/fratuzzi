# -*- coding: utf-8 -*-
from openerp import models, fields
class CompetenciaProject(models.Model):
    _name = 'competencia.project'
    _rec_name="competencia"
    competencia = fields.Char('Competência', required=True)