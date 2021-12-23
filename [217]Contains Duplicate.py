# Given an integer array nums, return true if any value appears at least twice i
# n the array, and return false if every element is distinct. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3,1]
# Output: true
#  Example 2: 
#  Input: nums = [1,2,3,4]
# Output: false
#  Example 3: 
#  Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics Array Hash Table Sorting 
#  👍 3189 👎 903


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
        
# leetcode submit region end(Prohibit modification and deletion)
