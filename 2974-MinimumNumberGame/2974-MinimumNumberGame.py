class�Solution:
����def�numberGame(self,�nums:�List[int])�->�List[int]:
��������nums.sort()
��������res�=�[]
��������for�i�in�range(0,�len(nums),�2):
������������res.extend([nums[i+1],�nums[i]])
��������return�res
