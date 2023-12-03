class�UnionFind:
����def�__init__(self,�size):
��������self.root�=�[i�for�i�in�range(size)]
��������self.rank�=�[1]�*�size

����def�find(self,�x):
��������if�x�==�self.root[x]:
������������return�x
��������self.root[x]�=�self.find(self.root[x])
��������return�self.root[x]

����def�union(self,�x,�y):
��������rootX�=�self.find(x)
��������rootY�=�self.find(y)
��������if�rootX�!=�rootY:
������������if�self.rank[rootX]�>�self.rank
[rootY]:
