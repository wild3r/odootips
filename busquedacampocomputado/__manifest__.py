# -*- coding: utf-8 -*-
# Copyright 2017, Wilder Hernández Garcìa,  Email: wilderhernandezg@gmail.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Busqueda de campos computados',
    'summary': 'Busqueda de campos computados o calculados.',
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
        'views/tree.xml',
        'views/search.xml',
    ],
}
