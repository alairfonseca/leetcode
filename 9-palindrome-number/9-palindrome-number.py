class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        aux = x
        
        while aux > 0:
            digit = aux % 10
            reverse = (reverse * 10) + digit
            aux //= 10
        
        return reverse == x