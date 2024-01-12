class�Solution:
����def�carPooling(self,�trips:�List[List[int]],�capacity:�int)�->�bool:
��������locations�=�[0]�*�1001
��������for�numPassengers,�start,�end�in�trips:
������������locations[start]�+=�numPassengers
������������locations[end]�-=�numPassengers
��������
��������for�numPassengers�in�locations:
������������capacity�-=�numPassengers
������������if�capacity�<�0:�return�False
��������
��������return�True

���
����def�carPooling2(self,�trips:�List[List[int]],�capacity:�int)�->�bool:
��������locations�=�[]
��������for�numPassengers,�start,�end�in�trips:
������������locations.extend([(start,�numPassengers),�(end,�-numPassengers)])
��������locations.sort()

[
