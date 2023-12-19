class�Solution:
����def�imageSmoother(self,�img:�List[List[int]])�->�
List[List[int]]:
��������m,�n�=�len(img),�len(img[0])
��������res�=�[[0]�*�n�for�_�in�range(m)]

��������for�i�in�range(m):
������������for�j�in�range(n):
����������������sum,�count�=�0,�0

����������������for�x�in�(i�-�1,�i,�i�+�1):
��������������������for�y�in�(j�-�1,�j,�j�+�1):
������������������������if�0�<=�x�<�m�and�0�<=�y�<�n:
����������������������������sum�+=�img[x][y]
����������������������������count�+=�1
����������������res[i][j]�=�sum�//�count
��������
