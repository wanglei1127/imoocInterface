#coding=utf-8
import requests
import json

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
            res = requests.get(url=url, params=data, headers=header)
        elif data != None and header == None:
            res = requests.get(url=url, params=data)
        elif data == None and header != None:
            res = requests.get(url=url, headers=header)
        else:
            res = requests.get(url=url)
        print(res.status_code)
        return res.json()

    def run_main(self,method,url,header=None,data=None):
        if method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)
        # return res