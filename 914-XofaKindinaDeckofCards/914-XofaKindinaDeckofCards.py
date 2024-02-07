class Solution(object):
    def hasGroupsSizeX(self, deck):
        vals = Counter(deck).values()
        return reduce(math.gcd, vals) >= 2
[
