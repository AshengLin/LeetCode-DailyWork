# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: s = "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: s = "{[]}"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 
#  👍 8361 👎 340


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'(': 1, ')': 6, '{': 2, '}': 5, '[': 3, ']': 4}
        temp_str = ""
        for i in range(len(s)):
            temp_str += str(char_map[s[i]])
            if len(temp_str) >= 2 and int(temp_str[-1]) + int(temp_str[-2]) == 7 and int(temp_str[-1]) > int(temp_str[-2]):
                temp_str = temp_str[:-2]
        return temp_str == ''
# leetcode submit region end(Prohibit modification and deletion)
