
import re
class BankNumberHitor():
    
    def hit(self, value):
        if type(value) != str:
            raise ValueError
        matches = re.finditer(r"622\d{3}\d{7,33}", value)
        new_matches = []
        for i in matches:
            start = i.start()
            end  = i.end()
            number = value[start:end]
            if self.check_bank_number(number):
                new_matches.append((start, end))
        return new_matches

    def check_bank_number(self, value):
        bin_num = int(value[0:6])
        user_num_str = value[6:-1]
        mark_num = int(value[-1])
        if bin_num < 622000 or bin_num > 622999:
            return False
        sum = 0
        for i, v in enumerate(value[:-1]):
            if i%2 == 0:
                sum += int(v)*2
            else:
                sum += int(v)
        c_mark_num = 10 - sum%10
        if c_mark_num == mark_num:
            return True
        else:
            return False