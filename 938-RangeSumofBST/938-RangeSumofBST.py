class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], 
low: int, high: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return
            if low <= node.val <= high:
                res += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        dfs(root)
        return res
