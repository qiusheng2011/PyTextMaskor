

import unittest

from src.maskexecuter.phone import hit
from src.maskexecuter.url.hit import UrlHitor
from src.maskexecuter.ip.hit import IpHitor
from src.maskexecuter.email.hit import EmailHitor
from src.maskexecuter.key_word.hit import KeyWordHitor
from src.maskexecuter.bank_number.hit import BankNumberHitor
from src.maskexecuter.cn_ccsn.hit import CnCcsnHitor
class TestHitor(unittest.TestCase):

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

    def test_keywords(self):
        hit = KeyWordHitor(["地址","快递"])
        locations = hit.hit("阿斯顿发送到发2286422556sdf@qq.com时代峰峻啊地址快递费")
        print(locations)
        self.assertIsNotNone(locations)
    
    def test_banknumber(self):
        hit = BankNumberHitor()
        locations = hit.hit("阿斯顿发送到发2286422556sdf@qq.com时代峰峻啊地址快递费6212262201023557228")
        print(locations)
        self.assertIsNotNone(locations)
    
    def test_cn_ccsn(self):
        hit = CnCcsnHitor()
        t = "asdfasdfa公示失信被执行人名单372522195108010416sdfa"
        locations = hit.hit(t)
        print(locations)
        for s,e in locations:
            print(t[s:e])
            
        self.assertIsNotNone(locations)