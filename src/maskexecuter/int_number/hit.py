
import re

class IntNumberHitor():
    
    def hit(self, value):
        if type(value) != str:
            raise ValueError()
        matches = re.finditer(r"\d+", value)
        return [(i.start(), i.end()) for i in matches] if matches else []
    