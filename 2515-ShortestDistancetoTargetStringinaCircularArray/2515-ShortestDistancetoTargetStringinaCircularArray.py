[
class Solution:
    def closetTarget(self, words: List[str], 
target: str, startIndex: int) -> int:
        i, j, l = startIndex, startIndex, len(words)
        for k in range(l//2 + 1):
            i, j = startIndex - k, startIndex + k
            if words[i % l] == target: return abs
(startIndex - i)
            if words[j % l] == target: return abs(j 
- startIndex)

        return -1
