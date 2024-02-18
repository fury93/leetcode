            freq[key] += 1
            key = ord(ch) - 97
            lastPos[key] = i
        
        maxFreq = max(freq)

        return ''.join(chr(ch+97) for _, ch in sorted(zip(lastPos, range(27))) if freq[ch] == maxFreq)
        for i, ch in enumerate(s):
        freq, lastPos = [0] * 26, [0] * 26
    def lastNonEmptyString(self, s: str) -> str:
class Solution:
"
