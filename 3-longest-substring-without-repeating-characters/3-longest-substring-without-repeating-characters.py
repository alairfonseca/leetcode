class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_subs_size = 1
        subs_start = 0
        subs_end = 0
        visited = {}
        
        if not s:
            return 0
        
        for (i, ch) in enumerate(s):
            if not ch in visited or visited[ch] < subs_start:
                subs_end = i + 1
                print(longest_subs_size, subs_end, subs_start)
                longest_subs_size = max(longest_subs_size, subs_end - subs_start)
            else:
                print(ch, visited[ch])
                subs_start = visited[ch] + 1
            visited[ch] = i
        
        return longest_subs_size