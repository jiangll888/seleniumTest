import sys,os
sys.path.append(os.path.join(os.getcwd(),".."))
import ddt
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os
import unittest
from base.get_case_data import GetCaseData
from log.log_record import LogRecord

get_data = GetCaseData()
data = get_data.get_case_data()
log = LogRecord()
logger = log.get_log()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://www.5itest.cn/register")
        cls.regsiter_b = RegisterBusiness(cls.driver)

    # @ddt.data(
    #     ["email","username","password","code","email_error","请输入有效的电子邮件地址","邮箱校验失败"],
    #     ["email@163.com", "u", "password", "code", "username_error", "字符长度必须大于等于4，一个中文字算2个字符", "用户名校验失败"],
    #     ["email1@163.com", "username1", "p", "code", "password_error", "最少需要输入 5 个字符", "密码格式校验失败"],
    # )
    @ddt.data(*data)

    @ddt.unpack
    def test_case(self,email,username,password,code,assert_type,assert_msg,message):
        res = self.regsiter_b.register_func(email,username,password,code,assert_type,assert_msg)
        self.assertTrue(res,message)
        logger.info("66666")
        self.assertTrue(False)

    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                pic_path = os.path.join("../pic/",case_name)
                self.driver.save_screenshot(pic_path+".png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.close_handle()

if __name__ == "__main__":
    # unittest.main()
    # get_data()
    fp = open("../report/test.html","wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    HTMLTestRunner.HTMLTestRunner(stream=fp,title="test",description="测试").run(suite)
