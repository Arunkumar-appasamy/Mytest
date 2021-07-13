{
    'name' : 'User Access Report',
    'version' : '1.1',
    'summary': 'User Access Rights Details',
    'sequence': 10,
    'depends' : ['base'],
    'data': ['views/user_access.xml', 'security/ir.model.access.csv', ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
