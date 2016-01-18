# coding=utf-8


# 引用urllib库
import urllib
# 引用cof中的配置&基本http方法
import cof.http as cofHttp
from cof.conf import MyCfg

class BaseHttp(object):
    def __init__(self):
        my_cfg = MyCfg('cfg.ini')
        my_cfg.set_section('s3_api')

        self.header = {
           "Content-Type": "application/json",
           "Accept": "application/json"
        }

        self.host = my_cfg.get('host')
        self.port = my_cfg.get('port')

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port


if __name__ == "__main__":
    base_http = BaseHttp()
    print base_http.get_host()
    print base_http.get_port()
