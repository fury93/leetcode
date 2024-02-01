class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        return sum((i // 9 + 1) * f for i, f in enumerate(freq))

"
