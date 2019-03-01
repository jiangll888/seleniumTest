from PIL import Image
from ShowapiRequest import ShowapiRequest
import requests
import time

class GetCode:
    def __init__(self,driver):
        self.driver = driver

    def get_code_image(self,code_element,filename):
        self.driver.save_screenshot(filename)
        #code_element = self.get_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = left + code_element.size['width']
        bottom = top + code_element.size['height']
        print(left, top, right, bottom)
        img = Image.open(filename)
        im = img.crop((left * 1.5, top * 1.5, right * 1.5, bottom * 1.5))
        im.save(filename)
        time.sleep(2)

    def get_code_num(self, filename):
        r = ShowapiRequest("http://route.showapi.com/184-4", "87917", "4081410d063b4e82968f75523e9b6253")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", filename)  # 文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text