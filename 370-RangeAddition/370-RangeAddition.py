����def�getModifiedArray(self,�length:�int,�updates:�List[List[int]]
)�->�List[int]:
��������res�=�[0]�*�length

��������for�start,�end,�diff�in�updates:
������������res[start]�+=�diff
������������end�+=�1
������������if�end�<�length:
����������������res[end]�-=�diff
��������
��������return�accumulate(res)
5
