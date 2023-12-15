class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a, b = map(set, zip(*paths))
        return (b - a).pop()
