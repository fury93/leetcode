[
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for height, pos in people:
            res.insert(pos, [height, pos])
        return res
