import random
import string

class GetRandomSt:  
    def __init__(self):
        self.length = 0
    
    def ul_str(self):
        # 大文字
        ul = string.ascii_uppercase
        return ul
    
    def lc_str(self):
        # 小文字
        lc = string.ascii_lowercase
        return lc
    
    def num_str(self):
        # 数字
        num = string.digits
        return num
        
    def sym_str(self):    
        # 記号
        sym = string.punctuation   
        return sym
    
    def get_random_string(self, length, letters):
        self.length = length
        self.letters = letters
        result_str = ''.join(random.SystemRandom().choice(self.letters) for i in range(self.length))
        return result_str
