class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shiftChar(ch, shift):
            return (ord(ch) - shift) % 26
        
        d = defaultdict(list)
        for s in strings:
            shift = ord(s[0])
            key = tuple(shiftChar(c, shift) for c in s)
            d[key].append(s)

        return d.values()

