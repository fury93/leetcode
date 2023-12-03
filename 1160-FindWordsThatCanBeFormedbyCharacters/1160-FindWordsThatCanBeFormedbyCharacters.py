class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt, res = Counter(chars), 0
        for w in words:
            cnt2 = Counter(w)
            if cnt2 <= cnt: res += len(w)

        return res

