class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]: return word
        return ''
["abc","car","ada","racecar","cool"]
["notapalindrome","racecar"]
["def","ghi"]
