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
#  ð 7144 ð 367


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
        while node.next:  # ç¨nodeå»è®ç¾å¨æ¯åæ¸äºå
            firstNode = firstNode.next  # æ¸ä¸å»
            node = node.next
            if nextNode:  # ç¢ºèªæ¯å¦å°æå¾äº
                nextNode = nextNode.next
        if firstNode:
            firstNode.next = nextNode  # æ¥ä¸
        return head
# leetcode submit region end(Prohibit modification and deletion)
