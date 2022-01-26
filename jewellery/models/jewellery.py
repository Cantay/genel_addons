from odoo import fields, models, api,_
from odoo.exceptions import UserError
import requests
import json
cookie = "aa"

class jewelleryProfile(models.Model):
    _name = "jewellery.profile"

    name = fields.Char(string="Owner", copy=False, default="Olga")
    jewellery_name = fields.Char("Jewellery Name", copy=False)
    jewellery_degree = fields.Char("Jewellery Degree", copy=False)
    certificate_date = fields.Date(string="Certificate Date")
    shape = fields.Char("Shape", copy=False)
    carat = fields.Char("Carat", copy=False)
    fluorescence = fields.Char("Fluorescence", copy=False)
    colour_grade = fields.Char("Colour Grade", copy=False)
    clarity_grade = fields.Char("Clarity Grade", copy=False)
    cut = fields.Char("Cut", copy=False)
    colour_grading_scale = fields.Char("Colour Grading Scale", copy=False)
    clarity_grading_scale = fields.Char("Clarity Grading Scale", copy=False)

    email = fields.Char(string="Email", copy=False)
    phone = fields.Char("Phone", copy=False)
    is_virtual_class = fields.Boolean(string="Virtual Class Support?")
    jewellery_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    estalish_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime("Open Date")
    jewellery_type = fields.Selection([('public','Public jewellery'),
                                    ('private', 'Private jewellery')],
                                   string="Type of jewellery",
                                   )
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
    jewellery_image = fields.Image(string="Upload jewellery Image", max_width=100,
                                max_height=100)
    jewellery_description = fields.Html(string="Description", copy=False)
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto "
                                                                     "Rank",
                               store=True, help="This is auto populate data "
                                                "based on jewellery type change.")

    @api.depends("jewellery_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.jewellery_type == "private":
                rec.auto_rank = 50
            elif rec.jewellery_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    @api.model
    def name_create(self, name):
        rtn = self.create({"name":name, "email":"abc@gmail.com"})
        return rtn.name_get()[0]

    def name_get(self):
        student_list = []
        for jewellery in self:
            print(self, jewellery)
            name = jewellery.name
            if jewellery.jewellery_type:
                name += " ({})".format(jewellery.jewellery_type)
            student_list.append((jewellery.id, name))
        return student_list
   
    @api.model
    def auth_To_Server(self):
        company = self.env['res.company'].sudo().search([('id','=', 1)])
        for item in company:
            x_url = item.x_url
            x_username = item.x_username
            x_password = item.x_password
            x_database_name = item.x_database_name
        url = 'http://' + x_url + '/web/session/authenticate'
        headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
            "Content-Type": "application/json"
            }
        myobj = {
            "jsonrpc": "2.0",
            "params": {
                "login": x_username,
                "password": x_password,
                "db": x_database_name
            }
        }
        x = requests.post(url, json = myobj, headers=headers)
        #print the response text (the content of the requested file):
        #return str(x.content)
        #response = x.json()
        #return str(response['jsonrpc'])
        #aşağıdaki işlemle önce json parse edildi sonra 0-52 ye kadar substring yapıldı
        global cookie
        cookie = ((x.headers)['Set-Cookie'])[0:51]
        return str(cookie)
        #-------------------------------------------------------------------

    @api.model
    def get_Inhouse_Customer(self):
        company = self.env['res.company'].sudo().search([('id','=', 1)])
        for item in company:
            x_url = item.x_url
        url = 'https://' + x_url + '/web/dataset/search_read'
        headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
            "Content-Type": "application/json",
            "Cookie": cookie
            }
        myobj = {
            "jsonrpc":"2.0","method":"call","params":{"model":"hotspot.hotel.guest.in_house","fields":["id","partner_id","display_name_gdpr","birthdate_gdpr","room","check_in_date","check_out_date","email_gdpr","missing_value"],"domain":[],"context":{"lang":"en_US","tz":"Europe/Istanbul","uid":40,"params":{"action":214,"min":1,"limit":80,"view_type":"list","model":"hotspot.hotel.guest.in_house","menu_id":271,"_push_me":0},"bin_size":1},"offset":0,"limit":80,"sort":""},"id":400224464
        }
        x = requests.post(url, json = myobj, headers=headers)
        #print the response text (the content of the requested file):
        #return str(x.content)
        #response = x.json()
        #return str(response['jsonrpc'])
        #aşağıdaki işlemle önce json parse edildi sonra 0-52 ye kadar substring yapıldı
        last_result = json.loads((x.content))['result']['length']
        company = self.env['res.company'].sudo().search([('id','=', 1)])
        for item in company:
            item['x_inhouse_customer_number'] = last_result
        return str(last_result)  

# Inheriting the Sale Order Model and Adding New Field
# https://www.youtube.com/watch?v=z1Tx7EGkPy0&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=9
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    jewellery_name = fields.Char(string='Jeweller Inh. 1')
    is_jewellery = fields.Boolean(string='Jeweller Inh. 2')

    def action_confirm(self):
        print("odoo mates")
        res = super(SaleOrderInherit, self).action_confirm()
        return res


class ResPartners(models.Model):
    _inherit = 'res.partner'

    # How to OverRide Create Method Of a Model
    # https://www.youtube.com/watch?v=AS08H3G9x1U&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=26
    @api.model
    def create(self, vals_list):
        res = super(ResPartners, self).create(vals_list)
        print("yes working")
        # do the custom coding here
        return res