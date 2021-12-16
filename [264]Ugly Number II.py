# An ugly number is a positive integer whose prime factors are limited to 2, 3, 
# and 5. 
# 
#  Given an integer n, return the nth ugly number. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 
# ugly numbers.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are li
# mited to 2, 3, and 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1690 
#  
#  Related Topics Hash Table Math Dynamic Programming Heap (Priority Queue) 
#  👍 3439 👎 195


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i, j = 0, 0
        while i < n:
            j += 1
            temp = j
            while (temp / 5).is_integer():
                temp /= 5
            while (temp / 2).is_integer():
                temp /= 2
            while (temp / 3).is_integer():
                temp /= 3
            if temp == 1:
                i += 1
        return j
# leetcode submit region end(Prohibit modification and deletion)
