# -*- coding: utf-8 -*-
{
    'name': "Grocery Manage",
   
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': " This module provides XYZ functionality for Odoos',",
   'summary': 'Kirana stores are shops that serve daily needs products and commonly used grocery items, ',     
        

    'author': "Gautamsinh Makwana",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',
   

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml'
    ],  
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'images':['static/description/a.jpeg'],
    'icon':['static/description/icon.png'],

    'installable' : True,
    'application' : True,
    'auto_install' : False ,
    'license':'LGPL-3'
    
}