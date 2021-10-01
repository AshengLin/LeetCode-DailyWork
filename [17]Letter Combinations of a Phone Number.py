# Given a string containing digits from 2-9 inclusive, return all possible lette
# r combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digit to letters (just like on the telephone buttons) is given b
# elow. Note that 1 does not map to any letters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  
#  Related Topics Hash Table String Backtracking 
#  👍 7474 👎 579


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        letter_set = []
        ans = []
        for i in digits:
            letter_set.append(d[int(i)])
        for s in letter_set[0]:
            ans.append(s)
        j = 1
        while j < len(letter_set):
            temp = []
            for k in letter_set[j]:
                for t in ans:
                    temp.append(t+k)
            ans = temp
            j += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
