[
class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0

        while j < len(chars):
            char, cnt = chars[j], 0
            while j < len(chars) and chars[j] == char:
                cnt += 1
                j += 1
            chars[i] = char
            i += 1
            if cnt > 1:
                for d in str(cnt):
                    chars[i] = d
                    i += 1

        return i
