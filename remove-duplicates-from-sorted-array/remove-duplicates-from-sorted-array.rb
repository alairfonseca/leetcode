#require 'set'

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    result = []
    
    nums.each_with_index { |val, i|
        if nums[i] == nums[i + 1] then
            nums[i] = nil
        end
    }
    
    nums.delete(nil)
end