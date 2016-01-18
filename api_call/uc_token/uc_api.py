# coding=utf-8
'''
@author: Administrator
'''
import json
import cof.http as cofHttp
from base.http import BaseHttp
from nd.rest.nd_uc import NdUc

class UC(BaseHttp):

    def __init__(self):
        BaseHttp.__init__(self)
#         self.host = '101uccenter.beta.web.sdp.101.com'
        self.host = 'ucbetapi.101.com'
        self.port = ''
        self.http_obj = cofHttp.HttpCurl(self.host, ssl = True)
        header = [
            "Accept: application/json",
            "Content-Type: application/json"
        ]
        self.http_obj.set_header(header)

    def get_tokens(self, username, password):
        """
        获取token
        """
        json_body = {
            "login_name":username,
            "password":password,
            #"org_name":org_name,
            #"imei":""
        }
        params = json.dumps(json_body)
        return self.http_obj.post('/v0.9/tokens', params, isjson=True)
    
    def get_bearer_tokens(self, username, password):
        """
        获取bearer_token
        """
        json_body = {
            "login_name":username,
            "password":password
        }
        params = json.dumps(json_body)
        return self.http_obj.post('/v0.9/bearer_tokens', params, isjson=True)

if __name__ == '__main__':
    uf = UC()
    username = '890707@zsnl_te'
    passwords = '123456'
    nd_uc_o = NdUc()
    pwd_md5 = nd_uc_o.get_password_md5(passwords)
#     print uf.get_bearer_tokens(username, pwd_md5)
    print uf.get_tokens(username, pwd_md5)