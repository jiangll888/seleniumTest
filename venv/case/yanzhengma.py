from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
from ShowapiRequest import ShowapiRequest
import requests

driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.ID,"getcode_num")))
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
# (x,y) = im.size
# x_s = int(x/1.5)
# y_s = int(y/1.5)
# out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
# out.save("../pic/test0.png")
# im1 = Image.open("../pic/test0.png")
img = im.crop((left*1.5,top*1.5,right*1.5,bottom*1.5))
img.save("../pic/test_crop.png")

r = ShowapiRequest("http://route.showapi.com/184-4","87755","cb14c940108e49ab8dc73be7308ccfae" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"../pic/test_crop.png") #文件上传时设置
res = r.post()
print(res)
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息

