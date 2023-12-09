[
class Solution:
    # O(N^2)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional
[TreeNode]:
        pos = {val: key for key, val in enumerate(inorder)}

        def dfs(l, r):
            if l > r: return None
            root = TreeNode(postorder.pop())
            root.right = dfs(pos[root.val]+1, r)
            root.left = dfs(l, pos[root.val]-1)
            return root

        return dfs(0, len(inorder) - 1)
    
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional
[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

