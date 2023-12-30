class Solution:
    def makeEqual(self, words: List[str]) 
-> bool:
        cnt = Counter()
        for w in words:
            cnt.update(w)

        return all(v % len(words) == 0 for 
v in cnt.values())
