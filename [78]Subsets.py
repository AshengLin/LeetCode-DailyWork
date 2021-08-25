# Given an integer array nums of unique elements, return all possible subsets (t
# he power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in a
# ny order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [[],[0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  All the numbers of nums are unique. 
#  
#  Related Topics Array Backtracking Bit Manipulation 
#  👍 6813 👎 122


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets(nums[1:]) + [x + [nums[0]] for x in self.subsets(nums[1:])] if nums else [[]]
        
# leetcode submit region end(Prohibit modification and deletion)
