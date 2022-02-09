
import re

class EmailHitor():
    
    def hit(self, value):
        if type(value) != str:
            raise ValueError()
        matches = re.finditer(r"[\da-zA-Z]@[a-z]\.[a-z]", value)
        return [(i.start(), i.end()) for i in matches)] if matches else []