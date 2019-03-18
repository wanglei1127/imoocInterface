import requests
# import json

class RunMain():
    def send_get(self,url,data):
        res = requests.get(url=url,data=data)
        return res

    def send_post(self,url,data):
        res = requests.post(url=url,data=data)
        return res

    def run_main(self,url,method,data):
        # res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    run = RunMain()
    url = 'https://coding.imooc.com/api/prelearn'
    data = {
        'token':'0e1f9768a6de44ad3f62f3f809241c36',
        'timestamp':'1551773496894',
        'uid':'1914562',
        'cid':'309',
        'secrect':'906108abe9d6dda2bf2a515f0301a017',
        'apiname':'prelearn'
    }
    res = run.run_main(url,'GET',data)
    print(res.json())


# url = 'http://yuanxian.letv.com/letv/vip2.ldo'
# data = {
#     'businessId':'10031',
#     'country':'86',
#     'pids':'24719',
#     'platforms':'141001',
#     'type':'getChargeInfo',
#     'sign':'eaa7116c5a2229bbe0648afdf1cd2656'
# }
# url = 'https://order.imooc.com/api/pay/consultlist'
# data = {
#     'timestamp':'1551772550941',
#     'uid':'1914562',
#     'cid':'309',
#     'secrect':'906108abe9d6dda2bf2a515f0301a017',
#     'token':'fd26bb0794dc9736e711130c0c8013bc',
#     'apiname':'newcourseinfo'
# }

