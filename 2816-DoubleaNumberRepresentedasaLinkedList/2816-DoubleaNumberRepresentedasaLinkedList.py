# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def add(node):
            if not node: return 1
            carry = add(node.next)
            node.val += carry
            if node.val > 9:
                node.val = 0
                carry = 1
            else:
                carry = 0
            
            return carry
        
        carry = add(head)
        if carry:
            head = ListNode(1, head)
        
        return head

