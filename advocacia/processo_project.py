# -*- coding: utf-8 -*-
from openerp import models, fields
class ProcessoProject(models.Model):
    _name = 'processo.project'
    _rec_name="processo"
    processo = fields.Char('Processo', required=True)
    #caso_id = fields.Many2one('project.project', 'Pasta')
    competencia = fields.Many2one('competencia.project', 'Competência')
