
import re

class KeyWordHitor():
    
    def __init__(self, keywords=None):
        self._keywords = keywords or []
    
    def hit(self, value):
        if type(value) !=  str:
            raise ValueError()
        re_pattern = "|".join([ f"({i})" for i in self._keywords])
        if not re_pattern:
            return []
        else:
            matches = re.finditer(re_pattern, value)
            return [(i.start(), i.end()) for i in matches] if matches else []