class OrderedStream:

    def __init__(self, n: int):
        self.idx = 1
        self.data = [None] * (n + 1)
        
    def insert(self, idKey: int, value: str) -> 
List[str]:
        self.data[idKey] = value
        while self.idx < len(self.data) and 
self.data[self.idx]:
            self.idx += 1

        return self.data[idKey:self.idx]
        


