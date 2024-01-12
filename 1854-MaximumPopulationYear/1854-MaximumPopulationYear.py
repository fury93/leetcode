class Solution:
    def maximumPopulation(self, 
logs: List[List[int]]) -> int:
        years, diff = [0] * 101, 
1950

        for start, end in logs:
            years[start - diff] += 1
            years[end - diff] -= 1

        maxPopulation, maxYear, 
population = 0, 0, 0
        for year, count in enumerate
(years):
            population += count
            
[
