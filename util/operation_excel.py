import xlrd

class OperationExcel:

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/InterfaceCase.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet的内容
    def get_data(self):
        # if file_name:
        #     # sheetid = sheet_id
        #     # filename = file_name
        #     data = xlrd.open_workbook(file_name)
        #     tables = data.sheets()[sheet_id]
        # else:
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某个单元格内容
    def get_cell_value(self,row,col):
        cell_value = self.data.cell_value(row,col)
        return cell_value

    # 写入数据

    # 根据对应的caseid，找到对应行的内容

    # 根据对应的caseid，找到对应的行号

    # 根据行号，找到该行的内容

    # 获取某一列的内容

if __name__ == '__main__':
    oper = OperationExcel()
    print(oper.get_data().nrows)
    print(oper.get_lines())
    cell_value = oper.get_cell_value(1,8)
    print(cell_value)
    # filename = '../dataconfig/InterfaceCase.xlsx'
    # sheetId = 0
    # res = oper.get_data(filename,sheetId).nrows
    # print(res)