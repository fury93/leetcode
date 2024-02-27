# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxL = 0
        def dfs(node):
            if not node: return -1
            leftL = dfs(node.left)
            rightL = dfs(node.right)
            nonlocal maxL
            maxL = max(maxL, leftL + rightL + 2)
            return 1 + max(leftL, rightL)

        dfs(root)
        return maxL

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        maxL = 0
        def dfs(node):
            if not node: return 0
            leftL = dfs(node.left)
            rightL = dfs(node.right)
            nonlocal maxL
            maxL = max(maxL, leftL + rightL)
            return 1 + max(leftL, rightL)

        dfs(root)
        return maxL