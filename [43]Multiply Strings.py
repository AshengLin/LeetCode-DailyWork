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
        for i in len(num2):
            for j in len(num1):
                temp = num2[-i-1] * num1[-j-1]
                part_ans[] = temp % 10
        
# leetcode submit region end(Prohibit modification and deletion)
