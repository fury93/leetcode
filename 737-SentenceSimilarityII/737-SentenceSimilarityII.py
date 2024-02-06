
        return True

class UnionFind:
    def __init__(self):
        uf = UnionFind()
        for w1, w2 in similarPairs:
            uf.union(w1, w2)
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and not uf.connected(w1, w2):
                return False
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

[
