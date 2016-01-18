# coding=utf-8
__author__ = 'Administrator'
import unittest
from hamcrest import *
import cof.restful as CoRestful
from api_call.parents.parents_api import ParentsApi


class ParentsTest(unittest.TestCase):

    def setUp(self):
        print 'start run parents test ......'
        self.rest_o = CoRestful.Restful()
        self.pa = ParentsApi()
    
    def tearDown(self):
        print 'run parents test complete......'
    
    def test_getinfo(self):
        """
     测试查询用户基础数据
        """
        pid = "21521"
        response = self.pa.getinfo(pid)
        print response
        data = self.rest_o.parse_response(response, 200, "查询用户基础数据失败")
        print data
        assert_that(data, has_key("parent_id"), "no parent_id response")
        assert_that(data, has_key("uc_id"), "no uc_id response")
        assert_that(data, has_key("parent_name"), "no parent_name response")
        assert_that(data, has_key("parent_nick_name"), "no parent_nick_name response")
        assert_that(data, has_key("email"), "no email response")
        assert_that(data, has_key("sex"), "no sex response")
        assert_that(data, has_key("area"), "no area response")
        assert_that(data, has_key("event_list"), "no event_list response")
        assert_that(data, has_key("birthday"), "no birthday response")
        assert_that(data, has_key("created_time"), "no created_time response")
        assert_that(data, has_key("mobile"), "no mobile response")
        assert_that(data, has_key("avatar"), "no avatar response")
        assert_that(data, has_key("children_count"), "no children_count response")
        assert_that(data, has_key("user_score"), "no user_score response")
        assert_that(data, has_key("questions_count"), "no questions_count response")
        assert_that(data, has_key("answers_count"), "no answers_count response")
        assert_that(data, has_key("select_children"), "no select_children response")
        assert_that(data, has_key("is_handpassword"), "no is_handpassword response")
        assert_that(data, has_key("full_energy"), "no full_energy response")
        assert_that(data, has_key("guide_json"), "no guide_json response")
        assert_that(data, has_key("parents_habits_json"), "no parents_habits_json response")

if __name__ == "__main__":
    unittest.main()

