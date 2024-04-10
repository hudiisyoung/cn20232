import unittest
import ddt
import requests
import hashlib
import time
def MyMd5(mystr):
    mdmystr=hashlib.md5(mystr.encode(encoding='utf-8')).hexdigest()
    return mdmystr
@ddt.ddt
class Maker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url="https://fanyi-api.baidu.com/api/trans/vip/translate"

    @ddt.file_data('mydata.yaml')
    def test_01(self,value):
        print(value)
        #设置预期结果
        ymydata=''
        if value=="hello":
            ymydata="你好"
        elif value=='world':
            ymydata='世界'
        elif value=="test":
            ymydata="测验"
        elif value=="student":
            ymydata='大学生'

        url = self.url
        mdmystr = MyMd5("20210507000816969"+value+"123456sGZsjo0Y2OThznTznsRT")
        data = {
            "q": value,
            "from": "en",
            "to": "zh",
            "appid": "20210507000816969",
            "salt": "123456",
            "sign": mdmystr
        }
        res = requests.get(url, params=data)
        rj = res.json()
        cmydata=rj['trans_result'][0]['dst']
        self.assertEqual(ymydata,cmydata,"测试未通过")

        time.sleep(2)


if  __name__ == '__main__':
    unittest.main()
