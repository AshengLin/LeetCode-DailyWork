# Given a string paragraph and a string array of the banned words banned, return
#  the most frequent word that is not banned. It is guaranteed there is at least o
# ne word that is not banned, and that the answer is unique. 
# 
#  The words in paragraph are case-insensitive and the answer should be returned
#  in lowercase. 
# 
#  
#  Example 1: 
# 
#  
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", 
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-b
# anned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banne
# d.
#  
# 
#  Example 2: 
# 
#  
# Input: paragraph = "a.", banned = []
# Output: "a"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= paragraph.length <= 1000 
#  paragraph consists of English letters, space ' ', or one of the symbols: "!?'
# ,;.". 
#  0 <= banned.length <= 100 
#  1 <= banned[i].length <= 10 
#  banned[i] consists of only lowercase English letters. 
#  
#  Related Topics Hash Table String 
#  👍 1180 👎 2429


# leetcode submit region begin(Prohibit modification and deletion)
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.findall(r"\w+", paragraph.lower())
        count = collections.Counter(x for x in paragraph if x not in banned)
        return count.most_common(1)[0][0]
# leetcode submit region end(Prohibit modification and deletion)
