import xlrd
from xlutils.copy import copy

class OperaExcel:

    def __init__(self,filename=None,sheet=None):
        if filename == None:
            self.filename = "../config/case_d.xls"
        else:
            self.filename = filename
        if sheet == None:
            self.sheet = 0
        else:
            self.sheet = sheet
        self.excel_data = self.read_excel()
        self.sheet_data = self.get_sheet_data()

    def read_excel(self):
        excel_data = xlrd.open_workbook(self.filename)
        return excel_data

    def get_sheet_data(self):
        sheet_data = self.excel_data.sheet_by_index(self.sheet)
        return sheet_data

    def get_rows_num(self):
        return self.sheet_data.nrows

    def get_cols_num(self):
        return self.sheet_data.ncols

    def get_value(self,row,col):
        if row >= self.get_rows_num() or col >= self.get_cols_num():
            return None
        return self.sheet_data.cell_value(row,col)

    def get_row_value(self,row):
        '''
        获取整行数据
        :param row:
        :return:
        '''
        if row >= self.get_rows_num():
            return None
        return self.sheet_data.row_values(row)

    def write_value(self,row,col,value):
        if row >= self.get_rows_num() or col >= self.get_cols_num():
            return None
        '''如果直接用self.excel_data会有问题，因为每次实例化一次之后，
        后续操作的数据都是刚开始实例化的数据，而不是最新的数据，
        会导致以前写入的数据丢失'''
        data = xlrd.open_workbook(self.filename)
        new_excel = copy(data)
        new_excel.get_sheet(0).write(row,col,value)
        new_excel.save(self.filename)

if __name__ == "__main__":
    o = OperaExcel("../config/case_key.xls")
    print(o.get_value(1,12))