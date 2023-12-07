class Solution:
    def sortString(self, s: str) -> str:
        res, cnt = [], Counter(s)

        while len(res) < len(s):
            for alphabet in string.ascii_lowercase, reversed(string.ascii_lowercase):
                for c in alphabet:
                    if cnt[c] > 0:
                        res.append(c)
                        cnt[c] -= 1

        return ''.join(res)


