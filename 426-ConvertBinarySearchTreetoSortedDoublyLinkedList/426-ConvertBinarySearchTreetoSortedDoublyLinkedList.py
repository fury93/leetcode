"""
#�Definition�for�a�Node.
class�Node:
����def�__init__(self,�val,�left=None,�right=None):
��������self.val�=�val
��������self.left�=�left
��������self.right�=�right
"""

class�Solution:
����def�treeToDoublyList(self,�root:�'Optional[Node]')�->�'Optional[Node]':
��������if�not�root:�return�root
��������
��������cur,�prev,�head,�stack�=�root,�None,�None,�[]

��������while�cur�or�stack:
������������while�cur:
����������������stack.append(cur)
����������������cur�=�cur.left
������������node�=�stack.pop()

������������if�not�head:
����������������head�=�node
������������
������������if�prev:
