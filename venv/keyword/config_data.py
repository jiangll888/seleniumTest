from util.opera_excel import OperaExcel


class ConfigData:
    def __init__(self,filename="../config/case_key.xls"):
        self.op = OperaExcel(filename)

    def get_case_id(self,row):
        value = self.op.get_value(row,0)
        if value == '':
            return None
        else:
            return value

    def get_case_name(self,row):
        value = self.op.get_value(row,1)
        if value == '':
            return None
        else:
            return value

    def get_opera_desc(self,row):
        value = self.op.get_value(row,2)
        if value == '':
            return None
        else:
            return value

    def get_opera_method(self,row):
        value = self.op.get_value(row,3)
        if value == '':
            return None
        else:
            return value

    def get_opera_element_key(self,row):
        value = self.op.get_value(row,4)
        if value == '':
            return None
        else:
            return value


    def get_opera_data(self,row):
        value = self.op.get_value(row,5)
        if value == '':
            return None
        else:
            return value

    def get_expect_element(self,row):
        value = self.op.get_value(row,6)
        if value == '':
            return None
        else:
            return value

    def get_expect_method(self,row):
        value = self.op.get_value(row, 7)
        if value == '':
            return None
        else:
            return value

    def get_expect_result(self,row):
        value = self.op.get_value(row,8)
        if value == '':
            return None
        else:
            return value

    def write_real_result(self,row,value):
        self.op.write_value(row,9,value)

    def get_lines(self):
        return self.op.get_rows_num()

    def get_is_run(self,row):
        value = self.op.get_value(row, 10)
        if value == '':
            return None
        else:
            return value

if __name__ == "__main__":
    c = ConfigData()
    print(c.write_real_result(7,"pass"))