# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val: idx for idx, val in enumerate(inorder)}
        self.idx = 0

        def dfs(l, r):
            if l > r: return None
            root = preorder[self.idx]
            self.idx += 1
            return TreeNode(
                root,
                dfs(l, pos[root]-1),
                dfs(pos[root] + 1, r)
            )

        return dfs(0, len(inorder) - 1)

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
