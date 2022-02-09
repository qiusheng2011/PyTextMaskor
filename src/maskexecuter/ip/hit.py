
import re


class IpHitor():

    def hit(self, value):
        if type(value) != str:
            raise ValueError()
        matches = re.finditer(r"([0-255]\.){4}", value)
        return [(i.start(), i.end()) for i in matches] if matches else []
