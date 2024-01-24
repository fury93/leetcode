class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.headId = 0
        self.streamSum = 0
        self.uid = 0
        self.data = [0] * size

    def next(self, val: int) -> float:
        self.uid += 1
        tailId = (self.headId + 1) % self.size
        self.streamSum += val - self.data[tailId]
        self.headId = tailId
        self.data[self.headId] = val
        return self.streamSum / min(self.size, self.uid)


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
[
