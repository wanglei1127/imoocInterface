#coding=utf-8
from util.operation_excel import OperationExcel
import data.data_config
from util.operation_json import OperationJson

class GetData:

    def __init__(self):
        self.oper_excel = OperationExcel()

    # 获取excel行数，即case个数
    def get_case_line(self):
        return self.oper_excel.get_lines()

    # 获取url
    def get_request_url(self,row):
        col = int(data.data_config.get_url())
        url = self.oper_excel.get_cell_value(row,col)
        return url

    # 获取是否执行
    def get_is_run(self,row):
        col = int(data.data_config.get_run())
        run = self.oper_excel.get_cell_value(row,col)
        if run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_request_method(self,row):
        col = int(data.data_config.get_request_way())
        url = self.oper_excel.get_cell_value(row,col)
        return url

    # 获取是否携带header
    def is_header(self,row):
        col = int(data.data_config.get_header())
        header = self.oper_excel.get_cell_value(row, col)
        if header == 'yes':
            return data.data_config.get_header_value()
        else:
            return None

    # 获取请求数据
    # def get_request_data(self,row):
    #     oper_json = OperationJson()
    #     col = int(data.data_config.get_data())
    #     request_data = self.oper_excel.get_cell_value(row, col)
    #     if request_data == '':
    #         return None
    #     else:
    #         return oper_json.get_data(request_data)
    # 这样写行不行？视频7-7 13分钟
    def get_request_data(self,row):
        col = int(data.data_config.get_data())
        request_data = self.oper_excel.get_cell_value(row, col)
        if request_data == '':
            return None
        else:
            return request_data

    # 通过获取关键字拿到json数据
    def get_json_data(self,row):
        oper_json = OperationJson()
        data = oper_json.get_data(self.get_request_data(row))
        return data


    # 获取预期结果
    def get_expect_value(self,row):
        col = int(data.data_config.get_expect())
        expect = self.oper_excel.get_cell_value(row,col)
        if expect == '':
            return None
        else:
            return expect