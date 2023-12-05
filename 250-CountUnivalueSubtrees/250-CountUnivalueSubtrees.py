# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node: return True
            isLeft = dfs(node.left) if node.left else True
            isRight = dfs(node.right) if node.right else True
            if (not isLeft or node.left and node.left.val != node.val) or \
                not isRight or node.right and node.right.val != node.val: return False
            self.res += 1
            return True
        dfs(root)
        return self.res
