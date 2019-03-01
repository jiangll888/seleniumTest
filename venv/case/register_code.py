from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import requests
from ShowapiRequest import ShowapiRequest
import random
import time

driver = webdriver.Chrome()
def driver_init():
    '''
    浏览器初始化
    :return:
    '''
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()

def get_element(id):
    '''
    获取元素
    :param id:
    :return:
    '''
    return driver.find_element_by_id(id)

def get_random_user():
    '''
    获取随机数
    :return:
    '''
    user_info = ''.join(random.sample("1234567890abcdefg",8))
    return user_info

def get_code_image(filename):
    '''
    裁剪图片
    :param filename:
    :return:
    '''
    driver.save_screenshot(filename)
    code_element = get_element("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = left + code_element.size['width']
    bottom = top + code_element.size['height']
    img = Image.open(filename)
    im = img.crop((left*1.5,top*1.5,right*1.5,bottom*1.5))
    im.save(filename)

def get_code_num(filename):
    '''
    解析验证码
    :param filename:
    :return:
    '''
    r = ShowapiRequest("http://route.showapi.com/184-4", "87755", "cb14c940108e49ab8dc73be7308ccfae")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", filename)  # 文件上传时设置
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text

def wait_element(id,time_wait=15):
    wait = WebDriverWait(driver,time_wait)
    wait.until(EC.visibility_of_element_located((By.ID,id)))

def run_main():
    driver_init()
    user_info = get_random_user()
    wait_element("register_email")
    get_element("register_email").send_keys(user_info + "@163.com")
    get_element("register_nickname").send_keys(user_info)
    get_element("register_password").send_keys("baimaonv08340822")
    filename = "../pic/test.png"
    get_code_image(filename)
    code = get_code_num(filename)
    get_element("captcha_code").send_keys(code)
    get_element("register-btn").click()
    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    run_main()
