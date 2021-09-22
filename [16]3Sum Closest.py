# Given an integer array nums of length n and an integer target, find three inte
# gers in nums such that the sum is closest to target. 
# 
#  Return the sum of the three integers. 
# 
#  You may assume that each input would have exactly one solution. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,0,0], target = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -104 <= target <= 104 
#  
#  Related Topics Array Two Pointers Sorting 
#  👍 4362 👎 205


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = []
        for t in range(N - 2):
            if t > 0 and nums[t] == nums[t - 1]:
                continue
            i, j = t + 1, N - 1

            while i < j:
                temp_sum = nums[t] + nums[i] + nums[j]
                closet_sum = min(temp_sum, closet_sum)
                if temp_sum <= closet_sum:
                    ans.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif temp_sum < 0:
                    i += 1  # 加大
                else:
                    j -= 1  # 縮小
        return ans

# leetcode submit region end(Prohibit modification and deletion)
