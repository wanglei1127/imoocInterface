#coding=utf-8
import requests
class RunMethod:

    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res


    def get_main(self,url,data=None,header=None):
        res = None
        if data != None and header != None:
            res = requests.get(url=url, params=data, headers=header).json()
        elif data != None and header == None:
            res = requests.get(url=url, params=data).json()
        elif data == None and header != None:
            res = requests.get(url=url, headers=header).json()
        else:
            res = requests.get(url=url).json()
        return res

    def run_main(self,method,url,header=None,data=None):
        if method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res