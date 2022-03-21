class Solution:
    def longestCommonPrefix(self, strs):
        longest_prefix = ""
        
        for i in range(len(strs[0])):
            add_char = True
            
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if strs[j][i] != strs[0][i]:
                        add_char = False
                else:
                    add_char = False
                    break

            if add_char:
                longest_prefix += strs[0][i]
            else:
                break
        
        return longest_prefix