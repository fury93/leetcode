            prev.next, prev = (cur:= Phone(i)), cur
    def __init__(self, maxNumbers: int):
        self.slots = [True] * maxNumbers # True -> is available
        self.phones = Phone(-1) # backbone
        prev = self.phones
        for i in range(maxNumbers):
class Phone:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class PhoneDirectory:

[
