# Given a string s, find the length of the longest substring without repeating c
# haracters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  Example 4: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table String Sliding Window 
#  👍 15720 👎 778


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Tuple
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        ans = 1
        if s.isspace():
            return 1
        if s:
            for i in range(len(s)):
                if substring.__contains__(s[i]):
                    if len(substring) > ans:
                        ans = len(substring)
                    substring = {}
                substring[s[i]] = i
                if len(substring) > ans:
                    ans = len(substring)
            return ans
        else:
            return 0
# leetcode submit region end(Prohibit modification and deletion)
