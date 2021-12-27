# Given an integer n, return true if it is a power of three. Otherwise, return f
# alse. 
# 
#  An integer n is a power of three, if there exists an integer x such that n ==
#  3x. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 27
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: n = 0
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: n = 9
# Output: true
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
# Follow up: Could you solve it without loops/recursion? Related Topics Math Rec
# ursion 
#  👍 630 👎 84


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        while (n/3).is_integer():
            n = n/3
        if n == 1:
            return True
        else:
            return False

        
# leetcode submit region end(Prohibit modification and deletion)
