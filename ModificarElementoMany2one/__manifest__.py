# -*- coding: utf-8 -*-
# Copyright 2017, Wilder Hernández Garcìa,  Email: wilderhernandezg@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Modificar elementos de un Many2one',
    'summary': 'Modifica nombre de los elementos de un campo Many2one',
    'version': '10.0.1.0.0',
    'category': 'sale',
    'website': 'https://odootips.com/',
    'author': 'Wilder Hernández García',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'sale',
    ],
    'data': [
        'views/form.xml',
    ],
}
