    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

from threading import Lock

class Foo:
    def __init__(self):
[1,2,3]
[1,3,2]
