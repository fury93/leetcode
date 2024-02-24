
        self.rank = [1] * size
    def __init__(self, size):
        self.root = [i for i in range(size)]

class UnionFind:
                    uf.reset(y)
        
        return filter(lambda x: uf.connected(x, firstPerson), range(n))
            
            for x, y in meetingGroups[t]:
                if not uf.connected(x, firstPerson):
                    uf.reset(x)

        for t in sorted(meetingGroups.keys()):
            for x, y in meetingGroups[t]:
                uf.union(x, y)

        meetingGroups = defaultdict(list)
        for x, y, time in meetings:
            meetingGroups[time].append([x, y])
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.union(0, firstPerson)
class Solution:
6
