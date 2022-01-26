# Given two non-negative integers, num1 and num2 represented as string, return t
# he sum of num1 and num2 as a string. 
# 
#  You must solve the problem without using any built-in library for handling la
# rge integers (such as BigInteger). You must also not convert the inputs to integ
# ers directly. 
# 
#  
#  Example 1: 
# 
#  
# Input: num1 = "11", num2 = "123"
# Output: "134"
#  
# 
#  Example 2: 
# 
#  
# Input: num1 = "456", num2 = "77"
# Output: "533"
#  
# 
#  Example 3: 
# 
#  
# Input: num1 = "0", num2 = "0"
# Output: "0"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num1.length, num2.length <= 104 
#  num1 and num2 consist of only digits. 
#  num1 and num2 don't have any leading zeros except for the zero itself. 
#  
#  Related Topics Math String Simulation 
#  👍 2815 👎 504


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        p = len(num1) - 1
        q = len(num2) - 1
        carry = 0  # 需要進位

        while p>=0 or q>=0 or carry:
            e1 = int(num1[p]) if p >= 0 else 0
            e2 = int(num2[q]) if q >= 0 else 0
            temp = e1 + e2 + carry
            carry = temp // 10
            ans = str(temp % 10) + ans
            p -= 1
            q -= 1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
