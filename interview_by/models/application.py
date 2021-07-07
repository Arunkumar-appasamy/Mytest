from odoo import fields, models
class ApplicationsTest(models.Model):
    _name = 'hr.applicant.interview'

    interview_id=fields.Many2one('hr.applicant', string='Interview ID', invisible = 'True')
    user_id = fields.Many2one('res.users', string="Responsible" )
    stage_id = fields.Many2one('hr.recruitment.stage', string = 'Level', widget = 'radio')
    comments = fields.Char(String = 'Comm')
    date = fields.Datetime(String = "date")
