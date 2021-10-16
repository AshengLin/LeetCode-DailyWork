# Given an array nums of n integers, return an array of all the unique quadruple
# ts [nums[a], nums[b], nums[c], nums[d]] such that: 
# 
#  
#  0 <= a, b, c, d < n 
#  a, b, c, and d are distinct. 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  
#  Related Topics Array Two Pointers Sorting 
#  👍 4285 👎 515


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        print('nums=', nums)
        ans = []
        # key : 兩端, 中間去夾擊target， 若湊出來都太大, 右邊下修， 反之
        (s, m1, m2, e) = (0, 1, len(nums)-2, len(nums)-1)
        while s+2 < e:
            if m1 == m2:
                if sum([nums[s], nums[m1], nums[m2], nums[e]]) < target:
                    s += 1
                else:
                    e -= 1
                (m1, m2) = (s+1, e-1)  # reset
            temp = [nums[s], nums[m1], nums[m2], nums[e]]
            if sum(temp) < target:
                m1 += 1
            elif sum(temp) > target:
                m2 -= 1
            else:
                if temp not in ans:
                    ans.append(temp)
                print('temp = ', temp)
                print('index = ', [s, m1, m2, e])
                m1 += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
