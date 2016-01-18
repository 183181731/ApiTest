# coding=utf-8
import cof.http as cofHttp
from base.http import BaseHttp

class ChildrenApi(BaseHttp):
    
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
    
    def temp_children(self, params):
        url = "/newme/v0.1/children/temp_child"
        return self.http_obj.post(url, params)
    
    def add_children(self, params):
        url = "/newme/v0.1/children"
        return self.http_obj.post(url, params)

if __name__ == "__main__":
    children= ChildrenApi()
#     fields = [
#     ('parent_id' , "21521")
#     ]
#     response = children.temp_children(fields)
#     print response
    fields = [
        ('child_id' , "10279712"),
        ('birthday' , "1231441241241"),
        ('child_name' , "tiantian"),
        ('password' , "123123"),
        ('sex' , "1"),
        ('user_id' , "21521")
    ]
    response = children.add_children(fields)
    print response
    
#     children= ChildrenApi()
#     
#     user_id = "194"
#     child_id = "641"
#     child_name = "neinei"
#     sex = "1"
#     birthday = "1256412121"
#     parents_sex = "1"
#     parents_nick_name = "parents_nick_name"
#     file_path = "E:/test.png"
#     url = "http://class.me.tmc/me-class-api/v0.1/children"
#     fields = [
#     ('user_id' , user_id),
#     ('child_id', child_id),
#     ('child_name', child_name),
#     ('sex', sex),
#     ('birthday', birthday),
#     ('parents_sex', parents_sex),
#     ('parents_nick_name', 'parents_nick_name'),
#     ('myfiles',(pycurl.FORM_FILE, file_path))
#     ]
#     print children.postchildren(fields)

