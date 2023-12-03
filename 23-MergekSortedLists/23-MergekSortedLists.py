[
class UnionFind:
    def __init__(self, n: int): 
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node) -> int:
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2) -> int:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2: return False

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root2
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root1] = root2
            self.rank[root1] += 1
        return True
    
