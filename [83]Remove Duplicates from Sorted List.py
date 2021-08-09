# Given the head of a sorted linked list, delete all duplicates such that each e
# lement appears only once. Return the linked list sorted as well. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,1,2]
# Output: [1,2]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 300]. 
#  -100 <= Node.val <= 100 
#  The list is guaranteed to be sorted in ascending order. 
#  
#  Related Topics Linked List 
#  👍 3008 👎 154


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans_node = head  # copy
        while ans_node:
            temp = ans_node.next
            while temp and temp.val == ans_node.val:  # check val
                temp = temp.next
            ans_node.next = temp  # skip duplicates
            ans_node = temp  # new_loc.
        return head

# leetcode submit region end(Prohibit modification and deletion)
