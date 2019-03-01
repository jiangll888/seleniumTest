from config_data import ConfigData
from opera_methods import OperaMethods
from log.log_record import LogRecord

class RunMain:
    def __init__(self):
        self.con = ConfigData()
        self.opera = OperaMethods()
        self.log = LogRecord()
        self.logger = self.log.get_log()

    def run_main(self):
        row_num = self.con.get_lines()
        for i in range(1,row_num):
            is_run = self.con.get_is_run(i)
            self.logger.info("44445")

            if is_run == "yes":
                opera_method = self.con.get_opera_method(i)
                opera_element_key = self.con.get_opera_element_key(i)
                opera_data = self.con.get_opera_data(i)
                expect_element_key = self.con.get_expect_element(i)
                expect_element_method = self.con.get_expect_method(i)
                expect_element_data = self.con.get_expect_result(i)

                method = getattr(self.opera, opera_method)
                if opera_element_key == None and opera_data == None:
                    method()
                elif opera_element_key != None and opera_data == None:
                    method(opera_element_key)
                elif opera_element_key == None and opera_data != None:
                    method(opera_data)
                else:
                    method(opera_element_key,opera_data)

                if expect_element_method:
                    expect_method = getattr(self.opera,expect_element_method)
                    if expect_element_key:
                        result = expect_method(expect_element_key,expect_element_data)
                    else:
                        result = expect_method(expect_element_data)
                    if result:
                        self.con.write_real_result(i,"pass")
                    else:
                        self.con.write_real_result(i, "fail")
        self.log.close_handle()

if __name__ == "__main__":
    r = RunMain()
    r.run_main()