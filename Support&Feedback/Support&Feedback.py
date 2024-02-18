

            elif (ln:= r - l + 1) > res.len:
                res = Result(l, ln)
        return words[res.start:res.start + res.len]

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans, cur_group = [], -1
        for word, group in zip(words, groups):
            if group != cur_group:
                ans.append(word)
                cur_group = group
        return ans
[
