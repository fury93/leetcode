class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(c1 == c2 for c1, c2 in zip_longest(chain(*word1), chain(*word2)))

    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        def getChar(words):
            for word in words:
                for char in word:
                    yield char
            yield None
            
        return all(c1 == c2 for c1, c2 in zip(getChar(word1), getChar(word2)))
