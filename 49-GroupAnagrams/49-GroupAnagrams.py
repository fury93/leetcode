class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            result[tuple(sorted(word))].append(word)
        return list(result.values())
