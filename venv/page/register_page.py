from base.get_by_local import GetByLocal

class RegisterPage:
    def __init__(self,driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_user_email_element(self):
        return self.get_by_local.get_element("email")

    def get_user_name_element(self):
        return self.get_by_local.get_element("user_name")

    def get_user_password_element(self):
        return self.get_by_local.get_element("password")

    def get_user_code_text_element(self):
        return self.get_by_local.get_element("code_text")

    def get_user_code_img_element(self):
        return self.get_by_local.get_element("code_image")

    def get_register_button_element(self):
        return self.get_by_local.get_element("register_button")

    def get_email_error_element(self):
        return self.get_by_local.get_element("email_error")

    def get_username_error_element(self):
        return self.get_by_local.get_element("username_error")

    def get_password_error_element(self):
        return self.get_by_local.get_element("password_error")

    def get_code_error_element(self):
        return self.get_by_local.get_element("code_error")

    def wait_email_element(self):
        return self.get_by_local.wait_element("email")