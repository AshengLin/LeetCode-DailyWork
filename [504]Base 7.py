# Given an integer num, return a string of its base 7 representation. 
# 
#  
#  Example 1: 
#  Input: num = 100
# Output: "202"
#  Example 2: 
#  Input: num = -7
# Output: "-10"
#  
#  
#  Constraints: 
# 
#  
#  -107 <= num <= 107 
#  
#  Related Topics Math 
#  👍 428 👎 188


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        sign = 1 if num >= 0 else -1
        num = abs(num)
        result = ''
        while num:
            result = str(num % 7) + result
            num //= 7
        return ('-' if sign < 0 else '') + result
        
# leetcode submit region end(Prohibit modification and deletion)
