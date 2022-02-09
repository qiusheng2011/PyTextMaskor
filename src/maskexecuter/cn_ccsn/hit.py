
import re


cn_xnums = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

cn_c_mapping = [1,0,10,9,8,7,6,5,4,3,2]

class CnCcsnHitor():

    def hit(self, value):
        if type(value) != str:
            raise ValueError()
        matches = re.finditer(r"(?<=[^\d])(\d{17}([0-9]|x))(?=[^\d])|^(\d{17}([0-9]|x))$", value) or []
        new_matches = []
        for i in matches:
            start = i.start()
            end = i.end()
            cn_ccsn = value[start: end]
            if self.check_cn_ccsn(cn_ccsn):
                new_matches.append((start, end))
        return new_matches

    def check_cn_ccsn(self, value):
        global cn_xnums, cn_c_mapping
        sum = 0
        mark_num = value[-1]
        if mark_num in ["x"]:
            mark_num = 10
        else:
            mark_num = int(mark_num)

        for i, v in enumerate(value[:-1]):
            sum += (cn_xnums[i] * int(v))
        c_mark_num = cn_c_mapping[sum % 11]
        if c_mark_num == mark_num:
            return True
        else:
            False
