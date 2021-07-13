# Given a string s, return the longest palindromic substring in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: "bb"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a"
# Output: "a"
#  
# 
#  Example 4: 
# 
#  
# Input: s = "ac"
# Output: "a"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consist of only digits and English letters (lower-case and/or upper-case), 
# 
#  
#  Related Topics String Dynamic Programming 
#  👍 11927 👎 739


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Tuple
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = []
        if s:
            for i in range(len(s)):
                if ans == [] or s[i-2] == s[i]:
                    ans.append(s[i])


        return ''.join(ans)
        
# leetcode submit region end(Prohibit modification and deletion)
