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
        start, max_len = 0, 0
        for i in range(len(s)):
            if i - max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:  # for max_len = 2, 4, ...
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:  # for max_len = 1, 3, ...
                start = i - max_len
                max_len += 1
        return s[start: start+max_len]
# leetcode submit region end(Prohibit modification and deletion)
