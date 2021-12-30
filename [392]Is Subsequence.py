# Given two strings s and t, return true if s is a subsequence of t, or false ot
# herwise. 
# 
#  A subsequence of a string is a new string that is formed from the original st
# ring by deleting some (can be none) of the characters without disturbing the rel
# ative positions of the remaining characters. (i.e., "ace" is a subsequence of "a
# bcde" while "aec" is not). 
# 
#  
#  Example 1: 
#  Input: s = "abc", t = "ahbgdc"
# Output: true
#  Example 2: 
#  Input: s = "axc", t = "ahbgdc"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 104 
#  s and t consist only of lowercase English letters. 
#  
# 
#  
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >
# = 109, and you want to check one by one to see if t has its subsequence. In this
#  scenario, how would you change your code? Related Topics Two Pointers String Dy
# namic Programming 
#  👍 3461 👎 262


# leetcode submit region begin(Prohibit modification and deletion)
import re
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new_t = '.*'
        for i in range(len(s)):
            new_t += (str(s[i])+'+.*')
        pattern = re.compile(new_t)
        match = pattern.match(t)
        return match
# leetcode submit region end(Prohibit modification and deletion)
