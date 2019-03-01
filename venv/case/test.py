from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
import requests

driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
print(driver.title)
print(EC.title_contains("注册"))
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.ID,"register_email")))
email_element = driver.find_element(By.ID,"register_email")
email_element.send_keys("jiangliulin@163.com")
driver.find_element_by_name("nickname").send_keys("jiangll")
driver.find_element_by_xpath('//input[@id="register_password"]').send_keys("baimaonv08340822")
#验证码
driver.save_screenshot("../pic/test.png")
code_element = driver.find_element_by_id("getcode_num")
pos = code_element.location
left = pos['x']
top = pos['y']
size = code_element.size
width = size['width']
height = size['height']
right = left + width
bottom = top + height
print(left,right,top,bottom)
im = Image.open("../pic/test.png")
img = im.crop((left*1.5,top*1.5,right*1.5,bottom*1.5))
img.save("../pic/test_crop.png")

r = ShowapiRequest("http://route.showapi.com/184-4","87755","cb14c940108e49ab8dc73be7308ccfae" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"../pic/test_crop.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
driver.find_elements_by_class_name("col-xs-7")[0].find_elements_by_class_name("input-lg")[0].send_keys(text)
driver.find_element_by_xpath("//button[contains(text(),'注册')]").click()
time.sleep(5)
# driver.quit()