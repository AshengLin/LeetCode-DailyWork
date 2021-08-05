# Given a non-negative integer x, compute and return the square root of x. 
# 
#  Since the return type is an integer, the decimal digits are truncated, and on
# ly the integer part of the result is returned. 
# 
#  Note: You are not allowed to use any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is
#  truncated, 2 is returned. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 231 - 1 
#  
#  Related Topics Math Binary Search 
#  👍 2352 👎 2539


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        for i in range(x):
            if (i+1) ** 2 > x:
                return i
#  Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.

# leetcode submit region end(Prohibit modification and deletion)
