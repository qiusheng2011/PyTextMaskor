

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
    INT_NUMBER = "int_number"
    # 关键词
    KEY_WORD = "key_word"
    # 地址
    ADDRESS = 'address'
    # 中文名称
    CN_NAME = 'cn_name'

class MaskMethod(Enum):
    """ 脱敏方法
    """
    REPLACE = "replace"
    # 能解密的加密
    ENCRYPT = "encrypt"
    # 无功能缺失的处理
    EMULATE = "emulate"
    # 完全删除
    DELETE = "delete"
    # 截取
    CUT = "cut"
    # 混淆
    CONFUSE = "confuse"

class Maskor():
    """ 脱敏器
    """

    def __init__(self) -> None:
        pass

    def text_mask(self, value, mask_method:MaskMethod=None, mask_scope:List[MaskType]=None, extend_info=None):
        """文本脱敏
        """
        pass

    def full_text_mask(self, value, mask_method:MaskMethod=None, mask_scope:List[MaskType]=None, extend_info=None):
        """ 全文脱敏 
        """
        pass
    
    def field_mask(self, value, mask_method:MaskMethod=None, mask_scope:List[MaskType]=None, extend_info=None):
        """字段脱敏
        """