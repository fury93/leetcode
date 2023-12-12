[
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        d = collections.defaultdict(list)
        q = collections.deque([(root, 0)])
        minCol = maxCol = 0

        while q:
            node, col = q.popleft()
            d[col].append(node.val)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))

        return [d[key] for key in range(minCol, maxCol+1)]
