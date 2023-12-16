[
        d, prefix = dict(), 0
        while cur:
            prefix += cur.val
            d[prefix] = cur
            cur = cur.next

        cur, prefix = dummy, 0
        while cur:
            prefix += cur.val
            cur.next = d[prefix].next
            cur = cur.next

        return dummy.next

    def removeZeroSumSublists2(self, head: 
Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
