        end = cur # save the last node
          
        mid = math.ceil(cnt / 2)
        while mid > 0:
            cur, mid = cur.next, mid - 1

        # 1(start1) -> 2(cur) -> 3(cur.next) -> 4(end)
            cur, cnt = cur.next, cnt + 1
        while cur.next != start1:
        cur, cnt = start1, 1
        end.next = start2
    def splitCircularLinkedList(self, start1: Optional[ListNode]) -> List[Optional[ListNode]]:
        # find the lenght and the last node
        # after interation cur will be the last node for block1
        start2 = cur.next
class Solution:
        cur.next = start1

        return [start1, start2]
        

[
