[
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res, diff = math.inf, math.inf
        def dfs(node):
            if not node: return
            
            curDiff = abs(node.val - target)
            if curDiff < diff:
                res = node.val
                diff = curDiff
            if target < node.val: dfs(node.left)
            else: dfs(node.right)

        dfs(root)


            nonlocal res, diff
#     def __init__(self, val=0, left=None, right=None):
# class TreeNode:
            elif curDiff == diff:
                res = min(res, node.val)
        return res
