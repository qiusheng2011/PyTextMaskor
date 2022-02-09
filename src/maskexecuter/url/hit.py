
import re

class UrlHitor():
    
    def hit(self, value):
        if type(value) != str:
            raise ValueError()
        matches = re.finditer(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", value)
        return  [ (i.start(), i.end())for i in matches]  if matches else []