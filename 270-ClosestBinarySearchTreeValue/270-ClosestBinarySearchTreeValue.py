[
   
    
        res, diff = math.inf, math.inf
        def dfs(node):
            if not node: return
            
            nonlocal res, diff
            curDiff = abs(node.val - target)
            if curDiff < diff:
                res = node.val
                diff = curDiff
            root = root.left if target < root.val else root.right
        return res
    def closestValue2(self, root: Optional[TreeNode], target: float) -> int:
            res = min(res, root.val, key = lambda x: (abs(x - target), x))
        while root:
        res = root.val
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
#         self.left = left
#         self.right = right
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
# Definition for a binary tree node.
