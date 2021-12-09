# You are given an integer array nums. You are initially positioned at the array
# 's first index, and each element in the array represents your maximum jump lengt
# h at that position. 
# 
#  Return true if you can reach the last index, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jum
# p length is 0, which makes it impossible to reach the last index.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  0 <= nums[i] <= 105 
#  
#  Related Topics Array Dynamic Programming Greedy 
#  👍 8989 👎 527


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0  # 最遠距離
        for i in range(len(nums)):
            if i > reach:  # 若i超過最遠距離，代表跳不到一個
                return False
            reach = max(reach, i+nums[i])
        return True
# leetcode submit region end(Prohibit modification and deletion)
