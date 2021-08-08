# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics Math Dynamic Programming Memoization 
#  👍 7575 👎 229


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def factorial(n: int) -> int:
        return 1 if (n == 1 or n == 0) else (n * Solution.factorial(n - 1))

    def climbStairs(self, n: int) -> int:
        c_two_steps = n // 2
        c_one_step = n % 2
        result = 0
        while c_two_steps >= 0:
            result += Solution.factorial(n=(c_two_steps + c_one_step)) / (Solution.factorial(n=c_two_steps) * Solution.factorial(n=c_one_step))
            c_two_steps -= 1
            c_one_step += 2
        return int(result)

# leetcode submit region end(Prohibit modification and deletion)
