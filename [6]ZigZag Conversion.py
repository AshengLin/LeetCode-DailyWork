# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number o
# f rows like this: (you may want to display this pattern in a fixed font for bett
# er legibility) 
# 
#  
# P   A   H   N
# A P L S I I G
# Y   I   R
#  
# 
#  And then read line by line: "PAHNAPLSIIGYIR" 
# 
#  Write the code that will take a string and make this conversion given a numbe
# r of rows: 
# 
#  
# string convert(string s, int numRows);
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#  
# 
#  Example 3: 
# 
#  
# Input: s = "A", numRows = 1
# Output: "A"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists of English letters (lower-case and upper-case), ',' and '.'. 
#  1 <= numRows <= 1000 
#  
#  Related Topics String 
#  👍 2614 👎 6280


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Tuple
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        num_array = [''] * numRows
        for i in range(len(s)):
            if numRows == 1:
                return s
            if (i % (2 * numRows - 2)) < numRows:
                num_array[i % (2 * numRows - 2)] += str(s[i])
            else:
                num_array[(2 * numRows - 2) * ((i // (2 * numRows - 2))+1) - i] += str(s[i])
        return ''.join(num_array)
# leetcode submit region end(Prohibit modification and deletion)
