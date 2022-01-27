

from enum import Enum
from typing import List

class MaskType(Enum):
    """ 脱敏内容类型
    """
    # 手机号
    PHONE = "phone"
    # 银行卡号
    BANK_NUMBER = "bank_number"
    # 邮箱
    EMAIL = "email"
    # 机密信息
    AK = "ak"
    # IP
    IP = "ip"
    # 中国公民身份证号码 citizens'credit security numbers
    CN_CCSN = "cn_ccsn"
    URL = ""
    # 纯数字
    INT_NUMER = "int_number"
    
    # 关键词
    KEY_WORD = "KEY_WORD"

class MaskMethod(Enum):
    """ 脱敏方法
    """
    REPLACE = "replace"
    # 能解密的加密
    ENCRYPT = "encrypt"
    # 无功能缺失的处理
    EMULATE = "emulate"
    DELETE = "delete"
    CUT = "cut"
    CONFUSE = "confuse"

class Maskor():
    """ 脱敏器
    """

    def __init__(self) -> None:
        pass

    def mapping_mask(self, value):
        return value

    def text_mask(self, value, mask_scope:List[MaskType]=None, extend_info=None):
        pass

    def full_text_mask(self, value):
        pass
    
    def field_mask(self,  value, mask_scope:List[MaskType]=None, extend_info=None):
        pass