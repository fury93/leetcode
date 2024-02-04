    def oddString(self, words: List[str]) -> str:
        eq = defaultdict(list)
        
        for w in words:
            diff = [ord(a)-ord(b) for a, b in zip(w[:-1], w[1:])]
            eq[tuple(diff)].append(w)

        for _, ws in eq.items():
            if len(ws) == 1:
                return ws[0]
class Solution:
[
