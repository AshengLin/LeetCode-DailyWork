# Implement strStr(). 
# 
#  Return the index of the first occurrence of needle in haystack, or -1 if need
# le is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great questio
# n to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty str
# ing. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
#  Input: haystack = "hello", needle = "ll"
# Output: 2
#  Example 2: 
#  Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  Example 3: 
#  Input: haystack = "", needle = ""
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  0 <= haystack.length, needle.length <= 5 * 104 
#  haystack and needle consist of only lower-case English characters. 
#  
#  Related Topics Two Pointers String String Matching 
#  👍 2711 👎 2592


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle == "":
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
