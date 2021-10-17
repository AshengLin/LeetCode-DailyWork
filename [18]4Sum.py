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
        board_1, board_2 = s, e
        while s+2 < e:
            temp = [nums[s], nums[m1], nums[m2], nums[e]]
            if sum(temp) < target:  # 掃內圈
                m1 += 1
            elif sum(temp) > target:
                m2 -= 1
            else:
                if temp not in ans:
                    ans.append(temp)
                print('append ans = ', [s, m1, m2, e])
                m1 += 1
            if m1 == m2:  # 判斷是否該移動s,e
                temp = [nums[s], nums[s+1], nums[e-1], nums[e]]
                if m1 + 1 == e or m1 - 1 == s:  # 查完這圈
                    test = [nums[board_1], nums[m1], nums[m2], nums[board_2]]
                    if sum(test) < target:
                        board_1 += 1
                    else:
                        board_2 -= 1
                    s, m1, m2, e = board_1, board_1+1, board_2-1, board_2
                    print('change board = ', [s, m1, m2, e])
                elif sum(temp) < target:
                    s += 1
                    print('change s', s)
                else:
                    e -= 1
                    print('change e', e)
                (m1, m2) = (s + 1, e - 1)


            print('end = ', [s, m1, m2, e])

        return ans
# leetcode submit region end(Prohibit modification and deletion)
