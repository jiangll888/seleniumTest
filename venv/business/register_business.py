from handle.register_handle import RegisterHandle

class RegisterBusiness:

    def __init__(self,driver):
        self.register_handle = RegisterHandle(driver)

    def user_base(self,email,name,passwd,code=None):
        self.register_handle.register_page.wait_email_element()
        self.register_handle.send_user_email(email)
        self.register_handle.send_user_name(name)
        self.register_handle.send_user_passwd(passwd)
        if code == None:
            code = self.register_handle.get_code_num()
        self.register_handle.send_user_code(code)
        self.register_handle.click_register_button()

    def register_func(self,email,username,password,code,assert_type,assert_msg):
        self.user_base(email,username,password,code)
        try:
            if self.register_handle.get_user_text(assert_type) in assert_msg:
                # print("邮箱校验成功")
                return True
        except:
            return False

    def register_email_error(self,email,name,passwd,code=None):
        '''
        邮箱错误
        :param email:
        :param name:
        :param passwd:
        :param code:
        :return:
        '''
        code = self.register_handle.get_code_num()
        self.user_base(email,name,passwd,code)
        try:
            if self.register_handle.get_user_text("email_error") in "请输入有效的电子邮件地址":
                print("邮箱校验成功")
                return True
        except:
            return False

    def register_name_error(self,email, name, passwd,code=None):
        '''
        用户名错误
        :param email:
        :param name:
        :param passwd:
        :param code:
        :return:
        '''
        code = self.register_handle.get_code_num()
        self.user_base(email, name, passwd, code)
        try:
            if self.register_handle.get_user_text("username_error") in "字符长度必须大于等于4，一个中文字算2个字符":
                print("用户名校验成功")
                return True
        except:
            return False

    def register_password_error(self,email, name, passwd,code=None):
        '''
        密码格式错误
        :param email:
        :param name:
        :param passwd:
        :param code:
        :return:
        '''
        code = self.register_handle.get_code_num()
        self.user_base(email, name, passwd, code)
        try:
            if self.register_handle.get_user_text("password_error") in "最少需要输入 5 个字符":
                print("密码校验成功")
                return True
        except:
            return False

    def register_code_error(self,email, name, passwd, code):
        '''
        验证码错误
        :param email:
        :param name:
        :param passwd:
        :param code:
        :return:
        '''
        self.user_base(email, name, passwd, code)
        try:
            if self.register_handle.get_user_text("code_error") in "验证码错误":
                print("验证码校验成功")
                return True
        except:
            return False

    def register_success(self,email, name, passwd,code=None):
        code = self.register_handle.get_code_num()
        self.user_base(email, name, passwd, code)
        try:
            if self.register_handle.register_page.get_register_button_element():
                print("注册失败")
                return False
        except:
            print("注册成功")
            return True