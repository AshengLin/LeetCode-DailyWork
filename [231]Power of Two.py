# Given an integer n, return true if it is a power of two. Otherwise, return fal
# se. 
# 
#  An integer n is a power of two, if there exists an integer x such that n == 2
# x. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1
# Output: true
# Explanation: 20 = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 16
# Output: true
# Explanation: 24 = 16
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  -231 <= n <= 231 - 1 
#  
# 
#  
# Follow up: Could you solve it without loops/recursion? Related Topics Math Bit
#  Manipulation Recursion 
#  👍 2527 👎 263


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while (n/2).is_integer() and n/2 > 0:
            n = n/2
        if n == 1:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
