# Given the head of a linked list, remove the nth node from the end of the list 
# and return its head. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
#  Follow up: Could you do this in one pass? 
#  Related Topics Linked List Two Pointers 
#  👍 7144 👎 367


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        for i in range(n):
            node = node.next
        if node == None:
            return head.next
        firstNode = head
        nextNode = head.next.next
        while node.next:  # 用node去讀現在是倒數了嗎
            firstNode = firstNode.next  # 數下去
            node = node.next
            if nextNode:  # 確認是否到最後了
                nextNode = nextNode.next
        if firstNode:
            firstNode.next = nextNode  # 接上
        return head
# leetcode submit region end(Prohibit modification and deletion)
