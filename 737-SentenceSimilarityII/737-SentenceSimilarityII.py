                self.rank[rootX] += 1

    def add(self, word):
        self.root[word] = word
        self.rank[word] = 1

    def connected(self, x, y):
        if x not in self.root or y not in self.root:
            return False
        return self.find(x) == self.find(y)
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
[
