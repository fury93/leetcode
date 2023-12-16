#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) 
-> Optional[ListNode]:
        dummy = prev = ListNode(0, head)

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.
val:
                    head = head.next
                prev.next = head.next
            else:
                prev = head

            head = head.next
        
