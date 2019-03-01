from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random

# path = r"E:\tools\selenium\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# path = r"E:\tools\selenium\edge\MicrosoftWebDriver.exe"
# driver = webdriver.Edge(executable_path=path)
driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
print(driver.title)
print(EC.title_contains("注册"))
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.ID,"register_email")))
email_element = driver.find_element(By.ID,"register_email")
# for i in range(5):
#     user_email = ''.join(random.sample("1234567890abcde", 8)) + "@163.com"
#     email_element.send_keys(user_email)
print(email_element.get_attribute("placeholder"))
email_element.send_keys("jiangliulin@163.com")
# print(email_element.get_attribute("value"))
# print(email_element.value_of_css_property("height"))
# driver.find_elements_by_class_name("input-lg")[0].send_keys("jiangliulin@163.com")
driver.find_element_by_name("nickname").send_keys("jiangll")
driver.find_element_by_xpath('//input[@id="register_password"]').send_keys("baimaonv08340822")
driver.find_elements_by_class_name("col-xs-7")[0].find_elements_by_class_name("input-lg")[0].send_keys("123456")
driver.find_element_by_xpath("//button[contains(text(),'注册')]").click()
driver.quit()