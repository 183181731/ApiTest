# coding=utf-8
__author__ = 'hq'

import sys
sys.path.insert(0, '..')

import random
import time
from uc_api import UC
from cof.rand import CoRand
import cof.restful as CoRestful
import base64
import hashlib
from hmac import new
from nd.rest.nd_uc import NdUc

class UCFactory(object):

    def __init__(self, host):
        self.uc = UC()
        self.nd_uc_o = NdUc()
        self.rest_o = CoRestful.Restful()
        self.rand_o = CoRand()
        self.host = host

    def get_tokens(self):
        """
        获取token
        """
        username = '890707@jzt_st'
        passwords = '123456'
        pwd_md5 = self.nd_uc_o.get_password_md5(passwords)
        response = self.uc.get_tokens(username, pwd_md5)
        return response

    def parse_tokens(self, response, http_method, request_url):
        """
        解析token
        """
        data_dec = self.rest_o.parse_response(response, 201, '解析token错误')
        mid = data_dec['access_token']
        mac_key = data_dec['mac_key']
        now = int(time.time())

        if len(str(now)) == 10:
            timestamp = str(now) + '000'
        else:
            timestamp = str(now)[0:9] + str(int(float(str(now)[9:])*1000))

        nonce = timestamp + ':' + self.rand_o.randomword(4) + str(random.randrange(1000, 9999))

        request_content = nonce + '\n' + http_method + '\n' + request_url + '\n' + self.host + '\n'
        mac = base64.b64encode(new(str(mac_key), str(request_content), digestmod=hashlib.sha256).digest())
        authorization = 'MAC id="' + str(mid) + '",nonce="' + str(nonce) + '",mac="' + str(mac) + '"'
        
        print authorization
        return str(authorization)
    
    def insert_authorization_to_header(self, http_obj, url, http_method):
        """
        在header中设置安全认证
        """
        response = self.get_tokens()
        authorization = self.parse_tokens(response, http_method, url)
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization":authorization
        }
        http_obj.set_header(header)
        return http_obj

if __name__ == '__main__':
    uf = UCFactory('101uccenter.beta.web.sdp.101.com')
    print uf.get_tokens()