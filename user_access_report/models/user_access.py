from odoo import api, fields, models
from odoo import tools

class UserAccessReport(models.Model):
    _name = "user.access.view"
    _auto = False
    _description = "User Access Report Details"

    login_id = fields.Char(comodel_name='res.users', string='Login', required=False, readonly=True)
    user_name = fields.Many2one(comodel_name='res.users', string='Name', required=False, readonly=True)
    user_department = fields.Many2one(comodel_name='hr.department', string='Department', required=False, readonly=True)
    work_address = fields.Many2one(comodel_name='res.partner', string='Company', required=False, readonly=True)
    application_name = fields.Many2one(comodel_name='ir.module.category', string='Menu', required=False, readonly=True)
    access_name = fields.Char(comodel_name='res.groups', string='Access Right', required=False, readonly=True)


    _depends = {'hr.employee': ['department_id', 'address_id','user_id'], 'res.groups': ['category_id', 'name'],}

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, 'user_access_view')
        self._cr.execute("""
            CREATE OR REPLACE VIEW user_access_view AS (
                SELECT
                    row_number() over() as id,
                    resuser.id as user_name,
                    resuser.login as login_id,
                    emp.department_id as user_department,
                    emp.address_id as work_address,
                    ref1.category_id as application_name,
                    ref1.name as access_name
                FROM res_users as resuser LEFT JOIN hr_employee as emp ON emp.user_id=resuser.id AND resuser.active=true
                LEFT JOIN(
                    SELECT res_groups.name,res_groups_users_rel.uid,res_groups.category_id
                    FROM res_groups LEFT JOIN res_groups_users_rel ON res_groups.id=res_groups_users_rel.gid ) as ref1 ON resuser.id=ref1.uid AND resuser.active=true
                )""")
