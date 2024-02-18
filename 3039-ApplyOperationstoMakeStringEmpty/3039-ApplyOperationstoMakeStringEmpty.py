    
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq, lastPos = defaultdict(int), defaultdict(int)
        for i, ch in enumerate(s):
        maxFreq = max(freq.values())

        return ''.join(ch for ch in sorted(lastPos, key=lastPos.get) if freq[ch] == maxFreq)
    def lastNonEmptyString2(self, s: str) -> str:
            freq[ch] += 1
            lastPos[ch] = i
        freq, lastPos = [0] * 26, [0] * 26
"
