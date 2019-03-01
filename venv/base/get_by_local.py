from util.read_ini import ReadIni
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GetByLocal:

    def __init__(self,driver):
        self.read = ReadIni()
        self.driver = driver

    def get_value(self,key,section="register"):
        value = self.read.get_ini_value(key,section)
        value_list = value.split(">")
        return value_list

    def get_element(self,key,section="register"):
        value_list = self.get_value(key,section)
        loc_type = value_list[0]
        loc_element = value_list[1]
        try:
            if loc_type == 'id':
                return self.driver.find_element_by_id(loc_element)
            else:
                return self.driver.find_element_by_xpath(loc_element)
        except:
            # self.driver.save_screenshot("../pic/element.png")
            print("元素未找到")
            return None

    def wait_element(self,key,section="register"):
        value_list = self.get_value(key, section)
        loc_type = value_list[0]
        loc_element = value_list[1]
        wait = WebDriverWait(self.driver,15)
        try:
            if loc_type == 'id':
                return wait.until(EC.visibility_of_element_located((By.ID,loc_element)))
            else:
                return wait.until(EC.visibility_of_element_located(By.XPATH,loc_element))
        except:
            # self.driver.save_screenshot("../pic/element.png")
            return None
            print("没等到元素出现")

