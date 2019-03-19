#coding=utf-8
import json

# fp = open('../dataconfig/request_data.json')
# data = json.load(fp)
# res = data['page2']
# print(res)

class OperationJson:

    def __init__(self):
        self.data = self.read_json()

    # 读取json文件
    def read_json(self):
        with open('../dataconfig/request_data.json') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self,id):
        data = self.data[id]
        return data

if __name__ == '__main__':
    opjson = OperationJson()
    data = opjson.get_data('page1')
    print(data)