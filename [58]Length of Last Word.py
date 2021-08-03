# Given a string s consists of some words separated by some number of spaces, re
# turn the length of the last word in the string. 
# 
#  A word is a maximal substring consisting of non-space characters only. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "Hello World"
# Output: 5
#  
# 
#  Example 2: 
# 
#  
# Input: s = "   fly me   to   the moon  "
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: s = "luffy is still joyboy"
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of only English letters and spaces ' '. 
#  There will be at most one word in s. 
#  
#  Related Topics String 
#  👍 1291 👎 3442


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        
# leetcode submit region end(Prohibit modification and deletion)
