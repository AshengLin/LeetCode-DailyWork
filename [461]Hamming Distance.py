# The Hamming distance between two integers is the number of positions at which 
# the corresponding bits are different. 
# 
#  Given two integers x and y, return the Hamming distance between them. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different
# .
#  
# 
#  Example 2: 
# 
#  
# Input: x = 3, y = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= x, y <= 231 - 1 
#  
#  Related Topics Bit Manipulation 
#  👍 2910 👎 196


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        x = bin(x)[2:]
        y = bin(y)[2:]
        m = max(len(x), len(y))
        if len(x) < len(y):
            x = '0'*(len(y)-len(x)) + x
        else:
            y = '0'*(len(x)-len(y)) + y
        for i in range(m):
            if x[i] != y[i]:
                count += 1
        return count

        return
        
# leetcode submit region end(Prohibit modification and deletion)
