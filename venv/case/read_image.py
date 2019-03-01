import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
import requests

image = Image.open("E:\\22.png")
testdata_dir_config = '--tessdata-dir "E:\\tools\selenium\\tesseract\\tessdata"'
text = pytesseract.image_to_string(image,config=testdata_dir_config)
print(text)


# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests

# r = ShowapiRequest("http://route.showapi.com/184-4","87755","cb14c940108e49ab8dc73be7308ccfae" )
# r.addBodyPara("typeId", "35")
# r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
# r.addFilePara("image", r"../pic/test_crop.png") #文件上传时设置
# res = r.post()
# print(res)
# text = res.json()['showapi_res_body']['Result']
# print(text) # 返回信息

