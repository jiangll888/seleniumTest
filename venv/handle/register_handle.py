from page.register_page import RegisterPage
import random
from util.get_code import GetCode
import os

class RegisterHandle:
    def __init__(self,driver):
        self.driver = driver
        self.register_page = RegisterPage(self.driver)
        self.get_c = GetCode(self.driver)

    def send_user_email(self,email):
        try:
            self.register_page.get_user_email_element().clear()
            self.register_page.get_user_email_element().send_keys(email)
        except:
            print("邮箱输入失败")

    def send_user_name(self,username):
        try:
            self.register_page.get_user_name_element().clear()
            self.register_page.get_user_name_element().send_keys(username)
        except:
            print("用户名输入失败")

    def send_user_passwd(self,password):
        try:
            self.register_page.get_user_password_element().clear()
            self.register_page.get_user_password_element().send_keys(password)
        except:
            print("密码输入失败")


    def send_user_code(self,code):
        try:
            self.register_page.get_user_code_text_element().clear()
            self.register_page.get_user_code_text_element().send_keys(code)
        except:
            print("验证码输入失败")

    def click_register_button(self):
        try:
            self.register_page.get_register_button_element().click()
        except:
            print("注册按钮点击失败")

    def get_user_text(self,info):
        try:
            if info == "email_error":
                return self.register_page.get_email_error_element().text
            elif info == "username_error":
                return self.register_page.get_username_error_element().text
            elif info == "password_error":
                return self.register_page.get_password_error_element().text
            else:
                return self.register_page.get_code_error_element().text
        except:
            return None

    def get_code_num(self,filename="../pic/code.png"):
        self.get_c.get_code_image(self.register_page.get_user_code_img_element(),filename)
        code_num = self.get_c.get_code_num(filename)
        return code_num

    def get_random_user(self):
        return ''.join(random.sample("1234567890abcde",8))



