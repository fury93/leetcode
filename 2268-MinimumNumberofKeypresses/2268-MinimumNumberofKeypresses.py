class Solution:
    def minimumKeypresses(self, s: str) -> int:
        val = sorted(Counter(s).values(), reverse=True)
        return sum(val[0:9]) + 2 * sum(val[9:18]) + 3 * sum(val[18:27])
"
