# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k
# ]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics Array Two Pointers Sorting 
#  👍 13053 👎 1263


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        for t in range(N - 2):
            if t > 0 and nums[t] == nums[t-1]:
                continue
            i, j = t + 1, N - 1
            while i < j:
                temp_sum = nums[t] + nums[i] + nums[j]
                if temp_sum == 0:
                    ans.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:  # 跳掉一樣的
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:  # 跳掉一樣的
                        j -= 1
                elif temp_sum < 0:
                    i += 1  # 加大
                else:
                    j -= 1  # 縮小
        return ans

# leetcode submit region end(Prohibit modification and deletion)
