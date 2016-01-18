# coding=utf-8
import cof.http as cofHttp
from base.http import BaseHttp

class ParentsApi(BaseHttp):
    
    def __init__(self):
        BaseHttp.__init__(self)
        self.host = self.get_host()
        self.port = self.get_port()
        self.http_obj = cofHttp.HttpCurl(self.host, self.port)
        authorization = "MAC id=\"child_mental_health-\",nonce=\"1\",mac=\"1\""

        self.header = [
            "Accept:application/json",
            "Authorization:" + authorization
        ]
        self.http_obj.set_header(self.header)   
         
    def getinfo(self, id):
        url = "/newme/v0.1/parents/" + id
        return self.http_obj.get(url)

if __name__ == "__main__":
    parents= ParentsApi()
    pid = "21521"
    print parents.getinfo(pid)
    
