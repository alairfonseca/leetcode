class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if nums[i] in known:
                return [known[nums[i]], i]
            else:
                known[comp] = i