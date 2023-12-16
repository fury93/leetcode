class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        cur, prev, head, stack = root, None, None, []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()

            if prev:
                node.left = prev
                prev.right = node
            else:
                head = node
            
            prev = node
            cur = node.right

        prev.right = head
        head.left = prev

        return head

