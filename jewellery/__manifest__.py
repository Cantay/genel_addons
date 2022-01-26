{
    'name':'jewellery',
    'version': '1.1',
    'author': 'Weblearns',
    'summary': "jewellery Management System",
    'sequence': 1,
    'description':"This is jewellery management system software suppored in "
                  "Odoo v13",
    'category':'jewellery',
    'website':'https://freeweblearns.blogspot.com',
    'depends':['base','sale'],
    'data':[
        "security/ir.model.access.csv",
        "views/jewellery_view.xml",
        "views/all_records_list.xml",
        "views/record_item.xml",
        "views/form_template.xml",
        "views/sale_order.xml",
        "reports/jewellery_report_views.xml"
    ]

}