            return sum(freq.keys()) == 1 # abc => can remove any symbol, but aabbcc => can't
        elif len(freq) == 1:
        if len(freq) > 2:
            return False
class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(Counter(word).values())
class Solution2:
    def equalFrequency(self, word: str) -> bool:

        for i in range(len(word)):
            
            if len(set(Counter(word[:i]+word[i+1:]).values()))==1:
                return True
        
        return False
        else:
            

# todo spend min 40+
"
