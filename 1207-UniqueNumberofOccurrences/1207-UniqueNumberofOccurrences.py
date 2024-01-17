class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> 
bool:
         return len(set(arr)) == len(set(Counter
(arr).values()))
[1,2,2,1,1,3]
[1,2]
