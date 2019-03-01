from configparser import ConfigParser

class ReadIni:
    def __init__(self,filename=None):
        if filename == None:
            self.filename = "../config/element.ini"
        else:
            self.filename = filename
        self.config = self.load_ini()

    def load_ini(self):
        config = ConfigParser()
        config.read(self.filename)
        return config

    def get_ini_value(self,key,section="register"):
        '''
        拿ini文件中的数据
        :param key:
        :param section:
        :return:
        '''
        try:
            value = self.config.get(section,key)
            return value
        except:
            print("文件读取错误")
            return None

if __name__ == '__main__':
    r = ReadIni()
    print(r.get_ini_value("email"))