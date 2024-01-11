#�Definition�for�a�binary�tree�node.
#�class�TreeNode:
#�����def�__init__(self,�val=0,�left=None,�right=None):
#���������self.val�=�val
#���������self.left�=�left
#���������self.right�=�right
class�Solution:
����def�maxAncestorDiff(self,�root:�TreeNode)�->�int:
��������if�not�root:
������������return�0

��������def�helper(node,�cur_max,�cur_min):
������������if�not�node:
����������������return�cur_max�-�cur_min
������������cur_max�=�max(cur_max,�node.val)
������������cur_min�=�min(cur_min,�node.val)
������������left�=�helper(node.left,�cur_max,�cur_min)
������������right�=�helper(node.right,�cur_max,�cur_min)
������������return�max(left,�right)

��������return�helper(root,�root.val,�root.val)
[8,3,10,1,6,null,14,null,null,4,7,13]
