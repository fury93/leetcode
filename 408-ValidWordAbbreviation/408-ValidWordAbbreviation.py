"
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def getShift(j):
            start = j
            while j < len(abbr) and abbr[j].isdigit():
                j += 1
            return int(abbr[start:j]), j

        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0': return False
                shift, j = getShift(j)
                i += shift
            
            if i >= len(word) or j >= len(abbr): break
            
            if word[i] != abbr[j]:
                return False
            
            i, j = i + 1, j + 1

        return i == len(word) and j == len(abbr)
        


0
