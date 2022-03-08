class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        symb = 1
        
        if x < 0:
            symb = -1
        
        x = abs(x)
        
        while x > 0:
            digit = x % 10
            x = x // 10
            
            result = (result * 10) + digit
        
        return 0 if result > 2 ** 31 else result * symb