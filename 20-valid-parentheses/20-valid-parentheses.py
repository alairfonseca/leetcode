class Solution:
    def isValid(self, s):
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif not len(stack) or pairs[stack.pop()] != ch:
                return False
        
        return len(stack) == 0