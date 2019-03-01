from util.opera_excel import OperaExcel

class GetCaseData:

    def __init__(self):
        self.op = OperaExcel()

    def get_case_data(self):
        data = []
        row_num = self.op.get_rows_num()
        for i in range(row_num):
            data.append(self.op.get_row_value(i))
        return data

if __name__ == "__main__":
    g = GetCaseData()
    print(g.get_case_data())