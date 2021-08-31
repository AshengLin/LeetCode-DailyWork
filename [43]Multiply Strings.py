# Given two non-negative integers num1 and num2 represented as strings, return t
# he product of num1 and num2, also represented as a string. 
# 
#  Note: You must not use any built-in BigInteger library or convert the inputs 
# to integer directly. 
# 
#  
#  Example 1: 
#  Input: num1 = "2", num2 = "3"
# Output: "6"
#  Example 2: 
#  Input: num1 = "123", num2 = "456"
# Output: "56088"
#  
#  
#  Constraints: 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 and num2 consist of digits only. 
#  Both num1 and num2 do not contain any leading zero, except the number 0 itsel
# f. 
#  
#  Related Topics Math String Simulation 
#  👍 2971 👎 1180


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for i in range(len(num2)):
            current = 0
            next = 0
            for j in range(len(num1)):
                multi = int(num2[-i-1]) * int(num1[-j-1])

                carry = multi // 10
                temp = multi % 10

                current += (temp + next) * (10 ** j)
                next = carry
            current += next * (10 ** len(num1))
            ans += current * (10 ** i)
        return str(ans)
# leetcode submit region end(Prohibit modification and deletion)
