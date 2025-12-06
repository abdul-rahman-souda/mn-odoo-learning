{
    "name":"App One",
    'author':"author",
    "category":"",
    "version":"17.0",
    "depends":[
        'base',
        'mail',
        "sale_management",
        # "accountant",
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
    ],
    'assets':{
        'web.assets_backend':['app_one/static/src/css/property.css']
    },
    'application':True
}