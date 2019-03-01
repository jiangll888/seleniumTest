from selenium import webdriver
from base.get_by_local import GetByLocal
from ShowapiRequest import ShowapiRequest
import random
from PIL import Image
import time

class RegisterFunc:

    def __init__(self,i,url="http://www.5itest.cn/register"):
        if i == 0:
            self.driver = webdriver.Chrome()
        elif i == 1:
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.get(url)
        self.driver.maximize_window()
        self.get_by_local = GetByLocal(self.driver)

    def get_random_user(self):
        user_info = ''.join(random.sample("1234567890abcdefg",8))
        return user_info

    def send_user_info(self,key,data):
        '''
        输入用户信息
        :param key:
        :param data:
        :return:
        '''
        self.get_element(key).send_keys(data)

    def get_element(self,key):
        '''
        获取元素信息
        :param key:
        :return:
        '''
        element = self.get_by_local.get_element(key)
        return element

    def user_click(self,key):
        '''
        点击操作
        :param key:
        :return:
        '''
        self.get_element(key).click()

    def get_code_image(self,filename):
        self.driver.save_screenshot(filename)
        code_element = self.get_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = left + code_element.size['width']
        bottom = top + code_element.size['height']
        print(left,top,right,bottom)
        img = Image.open(filename)
        im = img.crop((left*1.5,top*1.5,right*1.5,bottom*1.5))
        im.save(filename)

    def get_code_num(self,filename):
        r = ShowapiRequest("http://route.showapi.com/184-4", "87917", "4081410d063b4e82968f75523e9b6253")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", filename)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text


    def run_main(self ):
        self.get_by_local.wait_element("email")
        user_info = self.get_random_user()
        self.send_user_info("email",user_info + "@163.com")
        self.send_user_info("user_name",user_info)
        self.send_user_info("password","baimaonv08340822")
        filename = "../pic/test.png"
        self.get_code_image(filename)
        code_num = self.get_code_num(filename)
        #self.send_user_info("code_text",code_num)
        self.send_user_info("code_text","123")
        self.user_click("register_button")
        if self.get_element("code_error"):
            print("注册失败")
            self.driver.save_screenshot("../pic/codeerror.png")
        else:
            print("注册成功")
        # for i in range(2):
        #     if self.get_by_local.wait_element("code_error"):
        #         print("第"+str(i)+"次")
        #         time.sleep(1)
        #         filename = "../pic/test"+str(i)+".png"
        #         self.get_code_image(filename)
        #         code_num = self.get_code_num(filename)
        #         self.get_by_local.get_element("code_text").clear()
        #         self.get_by_local.get_element("code_text").send_keys(code_num)
        #         self.get_by_local.get_element("register_button").click()
        #     else:
        #         break

        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    # for i in range(3):
    #     r = RegisterFunc(i)
    #     # time.sleep(5)
    #     # print(r.get_element("email"))
    #     r.run_main()
    r = RegisterFunc(0)
    r.get_by_local.wait_element("email")
    r.send_user_info("email", 123)
    r.user_click("register_button")
    print(r.get_element("email_error").get_attribute("value"))
    print(r.get_element("email_error").text)