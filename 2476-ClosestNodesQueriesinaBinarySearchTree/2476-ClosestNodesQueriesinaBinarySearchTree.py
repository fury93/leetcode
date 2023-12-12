class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List
[List[int]]:
        self.nodes = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            self.nodes.append(node.val)
            dfs(node.right)
        dfs(root)

        res = []
        for val in queries:
            pos = bisect.bisect_left(self.nodes, val)
            
            if pos == len(self.nodes):
                res.append([self.nodes[pos-1], -1])
            elif self.nodes[pos] == val:
                res.append([val, val])
            elif pos == 0:
                res.append([-1, self.nodes[pos]])
            else:
                res.append([self.nodes[pos-1], self.nodes[pos]])

        return res
