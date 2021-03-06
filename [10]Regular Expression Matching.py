# Given an input string s and a pattern p, implement regular expression matching
#  with support for '.' and '*' where: 
# 
#  
#  '.' Matches any single character. 
#  '*' Matches zero or more of the preceding element. 
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, 
# by repeating 'a' once, it becomes "aa".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#  
# 
#  Example 4: 
# 
#  
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, i
# t matches "aab".
#  
# 
#  Example 5: 
# 
#  
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  1 <= p.length <= 30 
#  s contains only lowercase English letters. 
#  p contains only lowercase English letters, '.', and '*'. 
#  It is guaranteed for each appearance of the character '*', there will be a pr
# evious valid character to match. 
#  
#  Related Topics String Dynamic Programming Recursion 
#  👍 6239 👎 892


# leetcode submit region begin(Prohibit modification and deletion)
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ans = re.match(p, s)
        if ans is None:
            return False
        if ans.group(0) != s:
            return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
