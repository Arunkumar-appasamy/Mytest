from odoo import fields, models
class InterviewerBy(models.Model):
    _inherit = 'hr.applicant'

    interviewer_lines = fields.One2many('hr.applicant.interview', 'interview_id', string='Interviewer lines')
    
