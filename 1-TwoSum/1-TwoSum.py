class�Solution:
����def�twoSum2(self,�nums:�List[int],�target:�int)�->�List[int]:
��������seen�=�dict()�#�pairs�{value:�index}
��������
��������for�index,�value�in�enumerate(nums):
������������pairValue�=�target�-�value
������������if�pairValue�in�seen:
����������������return�[seen[pairValue],�index]
������������seen[value]�=�index

����def�twoSum(self,�nums:�List[int],�target:�int)�->�List[int]:
��������nums�=�sorted((value,�index)�for�index,�value�in�enumerate(nums))
��������l,�r�=�0,�len(nums)-1

��������while�l�<�r:
������������sm�=�nums[l][0]�+�nums[r][0]
������������if�sm�>�target:
����������������r�-=�1
������������elif�sm�<�target:
����������������l�+=1
������������else:
����������������break

��������return�[nums[l][1],�nums[r][1]]


[
