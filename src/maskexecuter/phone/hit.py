
import re
import time
class PhoneHitor():
    
    def hit(self, value):
        """ 匹配命中
        
        """
        value_type = type(value)
        tmp = ""
        if value_type == int:
            tmp = str(value)
        elif value_type == str:
            tmp = value
        else:
            raise ValueError("")
        a = time.time()
        match = re.finditer(r"((?<=[^\d])1\d{10}(?=[^\d]+)|(^1\d{10}$)|(^1\d{10}(?=[^\d]+))|((?<=[^\d])1\d{10}$))", tmp)
        print(f"cost:{(time.time()-a)*1000}ms")
        return [ (i.start(), i.end()) for i in match] if match else []



