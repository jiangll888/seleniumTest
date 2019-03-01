from business.register_business import RegisterBusiness
from selenium import webdriver

class FirstCase:
    def __init__(self,url="http://www.5itest.cn/register"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        self.regsiter_b = RegisterBusiness(driver)

    def test_register_email_error(self):
        email_error = self.regsiter_b.register_email_error("123","user123","111111","test1")
        if email_error:
            print("pass")
        else:
            print("fail")

    def test_register_name_error(self):
        name_error = self.regsiter_b.register_name_error("user123@163.com","u","111111","test1")
        if name_error:
            print("pass")
        else:
            print("fail")


    def test_register_password_error(self):
        passwd_error = self.regsiter_b.register_password_error("user123@163.com","user123","1","test1")
        if passwd_error:
            print("pass")
        else:
            print("fail")

    def test_register_code_error(self):
        code_error = self.regsiter_b.register_code_error("user123@163.com","user123","111111","test1")
        if code_error:
            print("pass")
        else:
            print("fail")

    def test_register_success(self):
        success = self.regsiter_b.register_success("user123","user123","111111","test1")
        if success:
            print("pass")
        else:
            print("fail")

if __name__ == "__main__":
    f = FirstCase()
    f.test_register_email_error()
    f.test_register_name_error()