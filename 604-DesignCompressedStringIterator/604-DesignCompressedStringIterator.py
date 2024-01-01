[
class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.pos = 0
        self.val = None
        self.cnt = 0
        self.__moveNext()
        
    def __moveNext(self):
        self.val = self.s[self.pos]
        pos = self.pos + 1
        while pos < len(self.s) and self.s[pos].isdigit():
            pos += 1
        self.cnt = int(self.s[self.pos+1:pos])
        self.pos = pos

    def next(self) -> str:
        if not self.hasNext(): return ' '
        if self.cnt == 0:
            self.__moveNext()
        self.cnt -= 1
        return self.val

    def hasNext(self) -> bool:
        return self.cnt > 0 or self.pos < len(self.s)
L
L
L
