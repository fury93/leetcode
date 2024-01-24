#·Definition·for·a·binary·tree·node.
#·class·TreeNode:
#·····def·__init__(self,·val=0,·left=None,·right=None):
#·········self.val·=·val
#·········self.left·=·left
#·········self.right·=·right
class·Solution:
····def·pseudoPalindromicPaths·(self,·root:·Optional[TreeNode])·->·
int:
········def·dfs(node,·paths):
············if·not·node:·return·0
············if·node.val·in·paths:
················paths.remove(node.val)
············else:
················paths.add(node.val)
············
············if·not(node.left·or·node.right):
················return·1·if·len(paths)·<=·1·else·0
············
············return·dfs(node.left,·set(paths))·+·dfs(node.right,·set
(paths))
····
········return·dfs(root,·set())


[2,3,1,3,1,null,1]
