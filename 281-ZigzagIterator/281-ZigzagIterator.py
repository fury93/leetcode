class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = list(filter(None, [v1, v2]))
        self.q = deque()
        for i in range(len(self.vectors)):
            self.q.append((i, 0))

    def next(self) -> int:
        vector, pos = self.q.popleft()
        val = self.vectors[vector][pos]
        if pos+1 < len(self.vectors[vector]):
            self.q.append((vector, pos+1))
        return val

    def hasNext(self) -> bool:
        return len(self.q) > 0
