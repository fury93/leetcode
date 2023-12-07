[
class Solution:
    def closetTarget(self, words: List[str], 
target: str, start: int) -> int:
        ln = len(words)
        for k in range(ln//2 + 1):
            l, r = start - k, start + k
            if words[l % ln] == target: return 
abs(start - l)
            if words[r % ln] == target: return 
abs(r - start)
        return -1
5
