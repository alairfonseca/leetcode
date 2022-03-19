class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        a = 0
        b = len(height) - 1

        while a < b:
            capacity = min(height[a], height[b]) * (b - a)

            if capacity > result:
                result = capacity

            if height[a] > height[b]:
                b -= 1
            else:
                a += 1

        return result