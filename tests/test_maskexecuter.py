

import unittest

from  src.maskexecuter.phone import hit_phone

class TestPhone(unittest.TestCase):

    def test_phone(self):
        hp = hit_phone.PhoneHitor()
        locations = hp.hit("18513279524sdfsdf")
        print(locations)