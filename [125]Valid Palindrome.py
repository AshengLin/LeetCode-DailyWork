# A phrase is a palindrome if, after converting all uppercase letters into lower
# case letters and removing all non-alphanumeric characters, it reads the same for
# ward and backward. Alphanumeric characters include letters and numbers. 
# 
#  Given a string s, return true if it is a palindrome, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric character
# s.
# Since an empty string reads the same forward and backward, it is a palindrome.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 105 
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 
#  👍 2713 👎 4563


# leetcode submit region begin(Prohibit modification and deletion)
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
