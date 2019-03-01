import unittest
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os

class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://www.5itest.cn/register")
        cls.regsiter_b = RegisterBusiness(cls.driver)

    def setUp(self):
        print("setup")

    def test_register01_email_error(self):
        email_error = self.regsiter_b.register_email_error("123","user123","111111")
        self.assertTrue(email_error,"邮箱检验失败")

    def test_register02_name_error(self):
        name_error = self.regsiter_b.register_name_error("user123@163.com","u","111111")
        self.assertTrue(name_error, "用户名检验失败")

    @unittest.skip("skip")
    def test_register03_password_error(self):
        passwd_error = self.regsiter_b.register_password_error("user123@163.com","user123","1")
        self.assertTrue(passwd_error, "密码格式检验失败")

    def test_register04_code_error(self):
        code_error = self.regsiter_b.register_code_error("user123@163.com","user123","111111","test1")
        self.assertTrue(code_error, "验证码检验失败")

    @unittest.skip("skip")
    def test_register05_success(self):
        success = self.regsiter_b.register_success("user123","user123","111111")
        self.assertTrue(code_error, "注册失败")

    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                pic_path = os.path.join("../pic/",case_name)
                self.driver.save_screenshot(pic_path+".png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest((FirstCase01("test_register01_email_error")))
    suite.addTest((FirstCase01("test_register02_name_error")))
    suite.addTest((FirstCase01("test_register03_password_error")))
    suite.addTest((FirstCase01("test_register04_code_error")))
    suite.addTest((FirstCase01("test_register05_success")))
    unittest.TextTestRunner().run(suite)
    # fp = open("../report/test.html","wb")
    # HTMLTestRunner.HTMLTestRunner(stream=fp,title="test",description="测试html report").run(suite)