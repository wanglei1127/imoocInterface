#coding=utf-8
import requests
import json

# url = 'https://www.imooc.com/apiw/logo'
# data = {
#     'callback':'jQuery21005556331848738598_1522560363404',
#     '_':'1522560363405'
# }
class RunMain():

    # def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)

    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        # return json.dumps(res,indent=2)
        return res

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        # return json.dumps(res,indent=2)
        return res

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)

        if method == 'POST':
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    run = RunMain()
    url = 'https://coding.m.imooc.com/api/courselist'
    data = {
    'page':2
    }
    res = run.run_main(url, 'GET', data)
    # url2 = 'https://coding.m.imooc.com/api/courselist'
    # data2 = {
    #     'page': 1
    # }

    # run2 = RunMain(url2,'GET',data2)
    print(res)
    print(type(res))
    # print(run2.res)

