# Given two integers dividend and divisor, divide two integers without using mul
# tiplication, division, and mod operator. 
# 
#  Return the quotient after dividing dividend by divisor. 
# 
#  The integer division should truncate toward zero, which means losing its frac
# tional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2. 
# 
#  Note: Assume we are dealing with an environment that could only store integer
# s within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, ass
# ume that your function returns 231 − 1 when the division result overflows. 
# 
#  
#  Example 1: 
# 
#  
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
#  
# 
#  Example 2: 
# 
#  
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
#  
# 
#  Example 3: 
# 
#  
# Input: dividend = 0, divisor = 1
# Output: 0
#  
# 
#  Example 4: 
# 
#  
# Input: dividend = 1, divisor = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  -231 <= dividend, divisor <= 231 - 1 
#  divisor != 0 
#  
#  Related Topics Math Bit Manipulation 
#  👍 2098 👎 7660


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return int(dividend/divisor) if (-2**31) <= int(dividend/divisor) <= (2**31-1) else (2**31-1)
# leetcode submit region end(Prohibit modification and deletion)
