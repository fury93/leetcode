[
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = defaultdict(int)
        for n in words:
            d[tuple(sorted(set(n)))] += 1

        return sum(v * (v-1) // 2 for v in d.values())
