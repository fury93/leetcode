class·Solution:
····def·majorityElement(self,·nums:·List[int])·->·int:
········majority,·cnt·=·0,·0

········for·n·in·nums:
············if·cnt·==·0:
················majority·=·n
············cnt·+=·(1·if·n·==·majority·else·-1)
········
········return·majority
[3,2,3]
[2,2,1,1,1,2,2]
