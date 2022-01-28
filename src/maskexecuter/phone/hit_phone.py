
import re

class PhoneHitor():
    
    def hit(self, value):
        value_type = type(value)
        tmp = ""
        if value_type == int:
            tmp = str(value)
        elif value_type == str:
            tmp = value
        else:
            raise ValueError("")
        match = re.search(r"1\d{10}", value)
        return list(match.regs) if match else []


