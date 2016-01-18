# coding=utf-8
__author__ = 'Administrator'
import unittest
from hamcrest import *
import cof.restful as CoRestful
from api_call.children.children_api import ChildrenApi

class ChildrenTest(unittest.TestCase):

    def setUp(self):
        print 'start run children test ......'
        self.rest_o = CoRestful.Restful()
        self.children = ChildrenApi()
    
    def tearDown(self):
        print 'run children test complete......'
    
    def test_add_children(self):
        """
        测试添加孩子数据
        """
        parent_id = "21521"
        fields = [
            ('parent_id' , parent_id)
        ]
        temp_response = self.children.temp_children(fields)
        temp_data = self.rest_o.parse_response(temp_response, 200, "生成child_id失败")
        print temp_data
        child_id = temp_data["child_id"]
        fields = [
            ('child_id' , str(child_id)),
            ('birthday' , "1231441241241"),
            ('child_name' , "tiantian"),
            ('password' , "123123"),
            ('sex' , "1"),
            ('user_id' , parent_id)
        ]
        add_response = self.children.add_children(fields)
        add_data = self.rest_o.parse_response(add_response, 200, "添加孩子失败")
        print add_data
        assert_that(add_data, has_key("child_name"), "no child_name response")
        assert_that(add_data, has_key("birthday"), "no birthday response")
        assert_that(add_data, has_key("sex"), "no sex response")
        assert_that(add_data, has_key("child_id"), "no child_id response")
        assert_that(add_data, has_key("imp_path"), "no imp_path response")
        assert_that(add_data, has_key("user_id"), "no user_id response")
        assert_that(add_data, has_key("password"), "no password response")

if __name__ == "__main__":
    unittest.main()