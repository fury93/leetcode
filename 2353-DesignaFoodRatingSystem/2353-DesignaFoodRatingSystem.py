from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List
[str], ratings: List[int]):
        self.cuisines = {}
        self.ratings = {}
        self.cuisinessFoods = defaultdict(SortedSet)

        for i, food in enumerate(foods):
            self.cuisines[food] = cuisines[i]
            self.ratings[food] = ratings[i]
            self.cuisinessFoods[cuisines[i]].add(
(-ratings[i], food))

    def changeRating(self, food: str, newRating: int) 
-> None:
