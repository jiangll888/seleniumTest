from config_data import ConfigData
from selenium import webdriver
import time
from util.get_code import GetCode
from base.get_by_local import GetByLocal

class OperaMethods:

    def start_browser(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def get_url(self,url):
        self.driver.get(url)

    def get_element(self,key):
        get_by_l = GetByLocal(self.driver)
        return get_by_l.get_element(key)

    def send_value(self,key,data):
        try:
            element = self.get_element(key)
            element.clear()
            element.send_keys(data)
        except:
            print("输入失败")

    def click(self,key):
        try:
            element = self.get_element(key)
            element.click()
        except:
            print("点击失败")

    def sleep_time(self,wait_time):
        time.sleep(wait_time)

    def quit_browser(self):
        self.driver.quit()

    def save_pic(self,filename):
        self.driver.save_screenshot(filename)

    def get_code_num(self,key,filename):
        element = self.get_element(key)
        get_c = GetCode(self.driver)
        get_c.get_code_image(element,filename)
        text = get_c.get_code_num(filename)
        return text

    def get_page_title(self,title):
        if title in self.driver.title:
            return True
        else:
            return False

    def get_user_info(self,key,info):
        element = self.get_element(key)
        if element == None:
            return False
        info_text = element.text
        if info in info_text:
            return True
        else:
            return False

