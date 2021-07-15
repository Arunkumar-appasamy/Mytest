# -- coding: utf-8

from odoo import api, fields, models
from odoo import tools

class UserAccessReport(models.Model):
    _name = "user.access.view"
    _auto = False
    _description = "User Access Report Details"

    login_id = fields.Char(string='Login')
    user_name_id = fields.Many2one('res.users', string='Name')
    hr_department_id = fields.Many2one('hr.department', string='Department')
    hr_manager_id = fields.Many2one('hr.employee',string='Manager')
    work_address_id = fields.Many2one('res.partner', string='Work Address')
    category_id = fields.Many2one('ir.module.category', string='Menu')
    access_id = fields.Char(string='Access Right')


    def init(self):
        tools.drop_view_if_exists(self._cr, 'user_access_view')
        self._cr.execute("""
            CREATE OR REPLACE VIEW user_access_view AS (
                SELECT
                    row_number() over() as id,
                    users.id as user_name_id,
                    users.login as login_id,
                    employee.department_id as hr_department_id,
                    employee.parent_id as hr_manager_id,
                    employee.address_id as work_address_id,
                    temp_table.category_id as category_id,
                    temp_table.name as access_id
                FROM 
                    res_users as users 
                LEFT JOIN
                    hr_employee as employee ON employee.user_id=users.id AND users.active=true
                LEFT JOIN
                    (SELECT res_groups.name,res_groups_users_rel.uid,res_groups.category_id
                    FROM res_groups LEFT JOIN res_groups_users_rel ON res_groups.id=res_groups_users_rel.gid ) as temp_table ON users.id=temp_table.uid AND users.active=true)""")
