#coding=utf-8
'''
比对预期结果与返回数据，如果返回数据中包含预期结果，则测试通过
'''
class CommonUtil:
    def is_contain(self,expect_data,response_data):
        if expect_data in response_data:
            flag = True
        else:
            flag = False
        return flag