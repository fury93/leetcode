[
#�"""
#�This�is�BinaryMatrix's�API�interface.
#�You�should�not�implement�it,�or�speculate�about�its�implementation
#�"""
#class�BinaryMatrix(object):
#����def�get(self,�row:�int,�col:�int)�->�int:
#����def�dimensions(self)�->�list[]:

class�Solution:
����def�leftMostColumnWithOne(self,�binaryMatrix:�'BinaryMatrix')�->�int:
��������rows,�cols�=�binaryMatrix.dimensions()
��������minCol�=�rows
��������for�row�in�range(rows):
������������l,�r�=�0,�minCol
������������while�l�<�r:
����������������col�=�(l�+�r)�//�2
����������������if�binaryMatrix.get(row,�col):
��������������������r�=�col
����������������else:
��������������������l�=�col�+�1
������������minCol�=�min(minCol,�l)
��������
��������return�minCol�if�minCol�<�cols�else�-�1

