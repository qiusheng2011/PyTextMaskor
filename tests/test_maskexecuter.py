

import unittest

from  src.maskexecuter.phone import hit
from src.maskexecuter.url.hit import UrlHitor
from src.maskexecuter.ip.hit import IpHitor
from src.maskexecuter.email.hit import EmailHitor
class TestPhone(unittest.TestCase):

    def test_phone(self):
        hp = hit.PhoneHitor()
        locations = hp.hit("18513279524sdfsdf")
        print(locations)
        blocations = hp.hit("18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf18513279524sdfsdf")
        print(blocations)
        self.assertIsNotNone(locations)
        self.assertIsNotNone(blocations)

    def test_url(self):
        hurl = UrlHitor()
        locations = hurl.hit("但是风沙大发https://192.168.0.207/zh-cn/3.9/library/re.html?highlight=re#match-objects的链接")
        print(locations)
        self.assertIsNotNone(locations)
    
    def test_ip(self):
        hip = IpHitor()
        locations = hip.hit("但是风沙大发https://192.168.0.207/zh-cn/3.9/library/re.html?highlight=re#match-objects的链接")
        print(locations)
        self.assertIsNotNone(locations)
    
    def test_email(self):
        hit = EmailHitor()
        locations = hit.hit("阿斯顿发送到发2286422556sdf@qq.com时代峰峻啊快递费")
        print(locations)
        self.assertIsNotNone(locations)