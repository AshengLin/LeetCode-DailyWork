# Given a signed 32-bit integer x, return x with its digits reversed. If reversi
# ng x causes the value to go outside the signed 32-bit integer range [-231, 231 -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed or
#  unsigned). 
# 
#  
#  Example 1: 
#  Input: x = 123
# Output: 321
#  Example 2: 
#  Input: x = -123
# Output: -321
#  Example 3: 
#  Input: x = 120
# Output: 21
#  Example 4: 
#  Input: x = 0
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  -231 <= x <= 231 - 1 
#  
#  Related Topics Math 
#  👍 5229 👎 7864


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Tuple
class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            new_x = int('-' + str(x)[1:][::-1])
        else:
            new_x = int(str(x)[0:][::-1])
        return new_x if 2**31 >= new_x >= -2**31 else 0
# leetcode submit region end(Prohibit modification and deletion)
