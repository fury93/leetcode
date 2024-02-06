class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(' ')
        trail = spaces - gap * (ln-1)
        return (' '*gap).join(words) + ' ' * trail
        gap = 0 if ln == 1 else spaces // (ln-1)
        ln = len(words)
        
"
