#coding=utf-8
from base.runmethod import RunMethod
from data.get_data import GetData
import json

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    def go_on_run(self):
        rows_count = self.data.get_case_line()
        res_arr = []
        for i in range(1,rows_count):
            print(i)
            url = self.data.get_request_url(i).strip()
            is_run = self.data.get_is_run(i)
            request_method = self.data.get_request_method(i)
            header = self.data.is_header(i)
            request_data = self.data.get_json_data(i)
            res = None
            if is_run:
                res = self.run_method.run_main(request_method,url,header,request_data)
            res_arr.append(res)
        return res_arr

if __name__ == '__main__':
    run = RunTest()
    res = run.go_on_run()
    for r in res:
        print(json.dumps(r,indent=2))