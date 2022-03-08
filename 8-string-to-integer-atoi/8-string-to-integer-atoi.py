class Solution:
    def clamp(self, x):
        minimum = -2 ** 31
        maximum = 2 ** 31 - 1
        
        if x > maximum:
            print(">")
            return maximum
        if x < minimum:
            print("<")
            return minimum
        print("x", x)
        return x
    
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0
        
        result = 0
        symbol = 1
        
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                symbol = -1
            
            s = s[1:]
        
        for ch in s:
            print(ch)
            if not ch.isdigit():
                break;
            
            result = (result * 10) + int(ch)
            print(result)
        
        return self.clamp(result * symbol)