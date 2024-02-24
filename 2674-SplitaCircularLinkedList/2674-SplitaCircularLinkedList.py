        end = cur
          
        mid = math.ceil(cnt / 2)
        while mid > 0:
            cur, mid = cur.next, mid - 1

        start2 = cur.next
            cur, cnt = cur.next, cnt + 1
        while cur.next != start1:
        cnt, cur, end = 1, start1, None
        end.next = start2
        cur.next = start1

        return [start1, start2]
        



[
