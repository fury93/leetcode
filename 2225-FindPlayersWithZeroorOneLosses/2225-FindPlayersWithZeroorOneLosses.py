class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(lambda: defaultdict(int))
        for w, l in matches:
            d[w][0] += 1
            d[l][1] += 1
        
        win, los = [], []
        for idx, stat in d.items():
            if stat[1] == 0:
                win.append(idx)
            elif stat[1] == 1:
                los.append(idx)
        
        return [sorted(win), sorted(los)]
[
