# Given an integer array nums, move all 0's to the end of it while maintaining t
# he relative order of the non-zero elements. 
# 
#  Note that you must do this in-place without making a copy of the array. 
# 
#  
#  Example 1: 
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#  Example 2: 
#  Input: nums = [0]
# Output: [0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -231 <= nums[i] <= 231 - 1 
#  
# 
#  
# Follow up: Could you minimize the total number of operations done? Related Top
# ics Array Two Pointers 
#  👍 7508 👎 208


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        n = len(nums)
        for i in range(n):  # 非0往前換
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j, n):  # j ~ n 都換成0
            nums[i] = 0

        
# leetcode submit region end(Prohibit modification and deletion)
