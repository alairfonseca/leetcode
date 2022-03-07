class Solution:
    def palindrome(self, s: str, a, b):
        while (a >= 0 and b < len(s)) and s[a] == s[b]:
            a -= 1
            b += 1
            
        return s[a + 1:b]

    def longestPalindrome(self, s: str) -> str:
        result = ""
        
        for i in range(len(s)):
            odd_pal = self.palindrome(s, i, i)
            even_pal = self.palindrome(s, i, i + 1)
            
            result = max(result, odd_pal, even_pal, key=len)
            
        return result
            
            